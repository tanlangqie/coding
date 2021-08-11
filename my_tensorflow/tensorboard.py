# -*- coding: utf-8 -*-#

# Name:   tensorboard.py
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
import matplotlib.pyplot as plt

def add_layer(inputs,in_size,out_size,n_layers,activation_function=None):
    layer_name = 'layer%s'%n_layers
    with tf.name_scope('layer'):
        with tf.name_scope('weights'):
            weights = tf.Variable(tf.random_uniform([in_size,out_size]))
            tf.summary.histogram(layer_name + '/weights',weights)       #可以观看变量的变化
        with tf.name_scope('biases'):
            biases = tf.Variable(tf.zeros([1,out_size]) + 0.1)
            tf.summary.histogram(layer_name + '/biases',biases)       #可以观看变量的变化

        with tf.name_scope('wx_plus_b'):
            wx_plus_b = tf.matmul(inputs,weights) + biases
        if activation_function is None:
            outputs = wx_plus_b
        else:
            outputs = activation_function(wx_plus_b)
        tf.summary.histogram(layer_name + '/outputs', outputs)  # 可以观看变量的变化

    return outputs

x_data = np.linspace(-1,1,300)[:,np.newaxis]    # (300,)-->(300,1)
# print(x_data.shape)

noise = np.random.normal(0,0.05,x_data.shape)
y_data = np.square(x_data) - 0.5 +noise

with tf.name_scope('inputs'):
    xs = tf.placeholder(tf.float32,[None,1],name='x_input')
    ys = tf.placeholder(tf.float32,[None,1],name='y_input')


l1 = add_layer(xs,1,10,n_layers=1,activation_function=tf.nn.relu)
prediction = add_layer(l1,10,1,n_layers=2,activation_function=None)

with tf.name_scope('loss'):
    loss = tf.reduce_mean(tf.reduce_sum(tf.square(ys-prediction),axis=1))
    tf.summary.scalar('loss',loss)                ### # 可以观看变量的变化
with tf.name_scope('train'):
    train_step = tf.train.GradientDescentOptimizer(0.1).minimize(loss=loss)



init = tf.global_variables_initializer()
sess = tf.Session()
merged = tf.summary.merge_all()                        #合并所有的summary
writer = tf.summary.FileWriter('logs/',sess.graph)     #执行后才有graph
sess.run(init)

for i in range(1000):
    sess.run(train_step,feed_dict={xs:x_data,ys:y_data})
    if i % 50:
        result = sess.run(merged,feed_dict={xs:x_data,ys:y_data})
        writer.add_summary(result,i)

#         try:
#             ax.lines.remove(lines[0])
#         except Exception:
#             pass
#
#         prediction_val = sess.run(prediction,feed_dict={xs:x_data,ys:y_data})
#         lines = ax.plot(x_data,prediction_val,'r-',lw=5)
#         plt.pause(0.1)