# -*- coding: utf-8 -*-#

# Name:   ww.py
# Author: tangzhuang
# Date:   2021/7/13
# desc:         

import pandas as pd
import sklearn as sklearn
from sklearn.feature_extraction import DictVectorizer
from sklearn import tree
import pydotplus
from sklearn.externals.six import StringIO
# pandas 读取 csv 文件，header = None 表示不将首行作为列
data = pd.read_csv('data/test.csv', header=None)
# 指定列
data.columns = ['Diet Habits', 'viviparous animal', 'Aquatic animals', 'Can fly','mammal']

# sparse=False意思是不产生稀疏矩阵
vec = sklearn.feature_extraction.DictVectorizer(sparse=False)
# 先用 pandas 对每行生成字典，然后进行向量化
feature = data[['Diet Habits', 'viviparous animal', 'Aquatic animals']]

X_train = vec.fit_transform(feature.to_dict(orient='record'))
# 打印各个变量
print('show feature\n', feature)
print('show vector\n', X_train)
print('show vector name\n', vec.get_feature_names())
print('show vector name\n', vec.vocabulary_)
Y_train = data['mammal']
clf = tree.DecisionTreeClassifier(criterion='entropy')
