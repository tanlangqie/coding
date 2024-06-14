# -*- coding: utf-8 -*-#

# Name:   lstm_life.py
# Author:
# Date:   2021/5/19
# desc:         

'''
多个变量多个特征的时间步数大于1  的  lstm 预测
'''

import pandas as pd
from math import sqrt
from keras import metrics
from numpy import concatenate
from matplotlib import pyplot as plt
import numpy as np
from pandas import concat
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import mean_squared_error
from keras.models import Sequential
from keras.layers import Dense, LSTM, Dropout

####################参数设置######################
n_hours = 6
myepoch = 50
n_features = 25
data_train = pd.read_csv(r'train_label(1).csv',header=0, index_col=0).iloc[:,2:]
cols_t = list(data_train.columns)
cols_t = ['life'] + cols_t[:-1]
data_test = pd.read_csv(r'test_label.csv',header=0, index_col=0).iloc[:,2:]
data_train = data_train[cols_t]
data_test = data_test[cols_t]
print(data_train.head())

#构造时间序列依赖特征
def series_to_supervised(data, n_in=1, n_out=1, dropnan=True):
    n_vars = 1 if type(data) is list else data.shape[1]
    df = pd.DataFrame(data)
    cols, names = list(), list()
    # input sequence (t-n, ... t-1)
    for i in range(n_in, 0, -1):
        cols.append(df.shift(i))
        names += [('var%d(t-%d)' % (j+1, i)) for j in range(n_vars)]
    # forecast sequence (t, t+1, ... t+n)
    for i in range(0, n_out):
        cols.append(df.shift(-i))
        if i == 0:
            names += [('var%d(t)' % (j+1)) for j in range(n_vars)]
        else:
            names += [('var%d(t+%d)' % (j+1, i)) for j in range(n_vars)]
    # put it all together
    agg = concat(cols, axis=1)
    agg.columns = names
    # drop rows with NaN values
    if dropnan:
        agg.dropna(inplace=True)
    return agg


# print(data.head())


values_train = data_train.values
values_test = data_test.values



# 将非整数的特征装欢为整数特征
# encoder = LabelEncoder()
# values[:,10] = encoder.fit_transform(values[:,10])


# 将特征归一化到0 -1之间
values_train = values_train.astype('float32')
values_test = values_test.astype('float32')


# normalize features
scaler = MinMaxScaler(feature_range=(0, 1))
scaled_train = scaler.fit_transform(values_train)
scaled_test = scaler.fit_transform(values_test)

###################################################################
# 构造时间序列特征
reframed_train = series_to_supervised(scaled_train, n_hours, 1)
reframed_test = series_to_supervised(scaled_test, n_hours, 1)
print(reframed_train.shape)
print(reframed_test.shape)


#####################     划分训练和测试数据集            ###################################
# split into train and test sets
values_train = reframed_train.values
values_test = reframed_test.values


train = values_train
test = values_test


# split into input and outputs
n_obs = n_hours * n_features
train_X, train_y = train[:, :n_obs], train[:, -n_features]
test_X, test_y = test[:, :n_obs], test[:, -n_features]
print(train_X.shape, len(train_X), train_y.shape)

# reshape input to be 3D [samples, timesteps, features]                         lstm需要的x的形状
train_X = train_X.reshape((train_X.shape[0], n_hours, n_features))
test_X = test_X.reshape((test_X.shape[0], n_hours, n_features))
print(train_X.shape, train_y.shape, test_X.shape, test_y.shape)





####################   定义网络    ####################


# design network
model = Sequential()
model.add(LSTM(100,return_sequences=True,   input_shape=(train_X.shape[1], train_X.shape[2])))
model.add(Dropout(0.3))
model.add(LSTM(100))
model.add(Dropout(0.3))
# model.add(LSTM(300))
# model.add(Dropout(0.3))
model.add(Dense(1))
model.compile(loss='mae', optimizer='adam')
# fit network
history = model.fit(train_X, train_y, epochs=myepoch, batch_size=512, validation_data=(test_X, test_y), verbose=2,
                    shuffle=False)


# 画出训练和测试集的损失
plt.title('loss')
plt.plot(history.history['loss'], label='train')
plt.plot(history.history['val_loss'], label='test')
plt.legend()
plt.show()
# #




######################################
# 预测
yhat = model.predict(test_X)
test_X = test_X.reshape((test_X.shape[0], n_hours*n_features))
print(test.shape)

# 将0 -1之间的数据在还原
inv_yhat = concatenate((yhat, test_X[:, -(n_features-1):]), axis=1)   #将预测的yhat和测试集的特征数据拼接在一起
inv_yhat = scaler.inverse_transform(inv_yhat)    #反转换，把0-1之间的数据还原至原来的大小
inv_yhat = inv_yhat[:,0]
# invert scaling for actual
test_y = test_y.reshape((len(test_y), 1))
inv_y = concatenate((test_y, test_X[:, -(n_features-1):]), axis=1)
inv_y = scaler.inverse_transform(inv_y)
inv_y = inv_y[:,0]



###############计算各种评价指标###################
# calculate RMSE
rmse = sqrt(mean_squared_error(inv_y, inv_yhat))
print('Test RMSE: %.2f' % rmse)

# MAE
mae = np.sum(np.absolute(inv_yhat-inv_y))/len(inv_y)     # (inv_y, inv_yhat)
print('Test MAE: %.2f' % float(mae))

# MAPE
def mymape(y_true, y_pred):
    return np.mean(np.abs((y_pred - y_true) / y_true)) * 100
mape1 = mymape(inv_y, inv_yhat)
print('Test MAPE: %.2f' % float(mape1))



#绘制真实值和预测值曲线
# x = pd.date_range(start='2017-02-27',freq='H',periods=48)
plt.title('life')
plt.plot( inv_y, color='green', label='true')
plt.plot( inv_yhat, color='red', label='pre')
plt.legend() # 显示图例
plt.xlabel('time')
plt.ylabel('life')
plt.show()
#
