# -*- coding: utf-8 -*-#

# Name:   mnist.py
# Author: tangzhuang
# Date:   2021/8/2
# desc:         

# -*- coding: utf-8 -*-#

# Name:   addLayer.py
# Author: tangzhuang
# Date:   2021/8/2
# desc:

import tensorflow as tf
import numpy as np
from tensorflow.examples.tutorials.mnist import input_data

mnist = input_data.read_data_sets("MNIST_data",one_hot=True)

def add_layer(inputs,in_size,out_size,activation_function=None):
    weights = tf.Variable(tf.random_uniform([in_size,out_size]))
    biases = tf.Variable(tf.zeros([1,out_size]) + 0.1)
    wx_plus_b = tf.matmul(inputs,weights) + biases
    if activation_function is None:
        outputs = wx_plus_b
    else:
        outputs = activation_function(wx_plus_b)
    return outputs

def compute_accuracy(v_xs,v_ys):
    global  prediction
    y_pre = sess.run(prediction,feed_dic={xs:v_xs})
    correct_prediction = tf.equal(tf.argmax(y_pre,1),tf.argmax(v_ys,1))
    accuracy = tf.reduce_mean(tf.cast(correct_prediction,tf.float32))
    result = sess.run(accuracy,feed_dict={xs:v_xs,ys:v_ys})
    return result

xs = tf.placeholder(tf.float32,[None,784])
ys = tf.placeholder(tf.float32,[None,10])


prediction = add_layer(xs,784,10,activation_function=tf.nn.softmax)

cross_entropy = tf.reduce_mean(-tf.reduce_sum(ys*tf.log(prediction),axis=1))

train_step = tf.train.GradientDescentOptimizer(0.5).minimize(cross_entropy)



init = tf.global_variables_initializer()
sess = tf.Session()
sess.run(init)


for i in range(1000):
    batch_xs ,batch_ys = mnist.train.next_batch(100)
    sess.run(train_step,feed_dict={xs:batch_xs,ys:batch_ys })
    if i % 50:
        # print(sess.run(loss,feed_dict={xs:x_data,ys:y_data}))
        print(compute_accuracy(mnist.test.images,mnist.test.label))