# -*- coding: utf-8 -*-#

# Name:   session.py
# Author: tangzhuang
# Date:   2021/8/1
# desc:    session的打开方式

import tensorflow as tf
import numpy as np
# tensorflow 2.5.0

matrix1 = tf.constant([[3,3]])       # 1*2
matrix2 = tf.constant([[2],[2]])     # 2 * 1

product = tf.matmul(matrix1,matrix2)      #np.dot


#method1
# sess = tf.Session()
# result = sess.run(product)
# print(result)
# print(result.shape)       #(1, 1)
# sess.close()



# method 2
with tf.Session() as sess:
    result2 = sess.run(product)
    print(result2)
