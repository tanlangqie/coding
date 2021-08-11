# -*- coding: utf-8 -*-#

# Name:   addLayer.py
# Author: tangzhuang
# Date:   2021/8/2
# desc:         

import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

def add_layer(inputs,in_size,out_size,activation_function=None):
    weights = tf.Variable(tf.random_uniform([in_size,out_size]))
    biases = tf.Variable(tf.zeros([1,out_size]) + 0.1)
    wx_plus_b = tf.matmul(inputs,weights) + biases
    if activation_function is None:
        outputs = wx_plus_b
    else:
        outputs = activation_function(wx_plus_b)
    return outputs

x_data = np.linspace(-1,1,300)[:,np.newaxis]    # (300,)-->(300,1)
# print(x_data.shape)

noise = np.random.normal(0,0.05,x_data.shape)
y_data = np.square(x_data) - 0.5 +noise

xs = tf.placeholder(tf.float32,[None,1])
ys = tf.placeholder(tf.float32,[None,1])


l1 = add_layer(xs,1,10,activation_function=tf.nn.relu)
prediction = add_layer(l1,10,1,activation_function=None)

loss = tf.reduce_mean(tf.reduce_sum(tf.square(ys-prediction),axis=1))

train_step = tf.train.GradientDescentOptimizer(0.1).minimize(loss=loss)


fig = plt.figure()
ax = fig.add_subplot(1,1,1)
ax.scatter(x_data,y_data)
plt.ion()   #show后不锁住画框，后面还可以用
plt.show()


init = tf.global_variables_initializer()
sess = tf.Session()
sess.run(init)


for i in range(1000):
    sess.run(train_step,feed_dict={xs:x_data,ys:y_data})
    if i % 50:
        # print(sess.run(loss,feed_dict={xs:x_data,ys:y_data}))

        try:
            ax.lines.remove(lines[0])
        except Exception:
            pass

        prediction_val = sess.run(prediction,feed_dict={xs:x_data,ys:y_data})
        lines = ax.plot(x_data,prediction_val,'r-',lw=5)
        plt.pause(0.1)