# -*- coding: utf-8 -*-#

# Name:   递归总结.py
# Author: tangzhuang
# Date:   2021/4/28
# desc:         




1.如果题目中出现 “所有，全部” 等字样，则代表需要遍历所有可能，此时应该想到递归。如果题目中还出现了
最大，最小，最长等字眼，则考虑动态规划

2.递归中要定义好递归函数的意义。传参数时候，list类型会每次都变，可以用res存储过程值，返回后求res_list的最值


3.在递归中，如果递归结果需要层层传递（即：所有递归只需要一个输出，则应该在fun中return fun ）如下所示
def fun(i, p):
    if i == 3:
        print('i=={}的输出'.format(i))
        return p
    return fun(i+1,p)

p = 5
print(fun(1, p))


4.暴力递归的改进----返回一个列表，在求列表的最值----》直接返回最值

import copy


#暴力递归------返回一个列表，在求列表的最值
# def fun(arr,count,i,path,res):
#     # print(id(path))
#     #count代表取了几只股票，如果已经取了两支了，则返回
#     if count == 2:
#         res.append(path)
#         return
#     if i == len(arr):
#         return
#     path = copy.deepcopy(path)
#     #不要第i个
#     fun(arr,count,i+1,path,res)
#
#     #要第i个
#     path.extend([arr[i]])
#     fun(arr,count+1,i+1,path,res)
#


#暴力递归 改进 --- 不需要列表，直接返回最值
def fun(arr,count,i,path,res):
    # print(id(path))
    if count == 2:
        return path[1] - path[0]
    if i == len(arr):
        return -100
    path = copy.deepcopy(path)
    #不要第i个
    a = fun(arr,count,i+1,path,res)

    #要第i个
    path.extend([arr[i]])
    b = fun(arr,count+1,i+1,path,res)
    return max(a,b)

arr = [2,1,5,7,3]
count = 0
path = []
i = 0
res = []

t = fun(arr,count,i,path,res)
print(t)