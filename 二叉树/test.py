# -*- coding: utf-8 -*-#

# Name:   test.py
# Author: tangzhuang
# Date:   2021/6/17
# desc:         

def fun(i, p):
    if i == 3:
        print('i=={}的输出'.format(i))
        return p
    return fun(i+1,p)

p = 5
print(fun(1, p))