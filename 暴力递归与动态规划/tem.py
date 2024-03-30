# -*- coding: utf-8 -*-#

# Name:   tem.py
# Author: tangzhuang
# Date:   2021/7/17
# desc:         

def fun(i, path,res):
    if i == 3:
        res.append(path)
        return
    # for k in range(i):
    print("i=={},{}".format(i,id(path)))
    fun(i+1, path+[i],res)
    return

path = []
print(id(path))
res = []
fun(1, path,res)
print(res)
# print(id(path))
# print(path)
print(['a']+['b'])