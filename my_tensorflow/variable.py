# -*- coding: utf-8 -*-#

# Name:   variable.py
# Author: tangzhuang
# Date:   2021/8/2
# desc:   variable

import tensorflow as tf

state = tf.Variable(0,name='counter')
print(state.name)

one = tf.constant(1)

new_value = tf.add(state , one)
update = tf.assign(state,new_value)    # 将new_value的值加载到stateli

init = tf.global_variables_initializer()

with tf.Session() as sess:
    sess.run(init)
    for i in range(3):
        sess.run(update)
        print(sess.run(state))
        # print(sess.run(update))




