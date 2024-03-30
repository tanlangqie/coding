# -*- coding: utf-8 -*-#

# Name:   test.py
# Author: tangzhuang
# Date:   2021/3/27
# desc:         

# num = [[0 for i in range(1,5)]for j in range(5)]
# a = [0 for i in range(1,5)]
# print(a)
# print(num)
#
# string = "abc"
# path = []
# res = []
#
# def fun(string,i,path,res):
#     if i >= len(string):
#         res.append(path)
#         return
#     #要第i个位置的值
#     fun(string,i+1,path[:]+[string[i]],res)
#     #不要第i个位置的值
#     fun(string,i+1,path[:],res)
#     return
# fun(string,0,path,res)
# for ss in res:
#     print(ss)
# print(res)
# print(string[0])
# print(string[1])
# print(string[2])
#
#
# path = [1]
# def fun(path,s):
#     if s==0:
#         return
#     print(id(path))
#     # path.append(2)
#     fun(path+[2],s-1)
#     return
# fun(path,3)
# print(path)

# pp= set()
# pp.add(1)
# pp.add(2)
# pp.add(1)
# print(pp)


#初版递归，递归函数不返回目标值，递归函数只是遍历一遍所有可能，由path记录路径，res统计每条路径对应的目标 结果，在递归函数的外层在去处理res的结果
def bag_digui2(w,v,index,rest,path,res):

    #base case 1
    if rest <= 0:
        res.append(sum(path))
        return
    #base case 2
    if index == len(w):
        res.append(sum(path))
        return

    #不要第i个物品
    bag_digui2(w,v,index+1,rest,path[:],res)

    #要第i个物品
    p2 = -1
    if rest >= w[index]:
        bag_digui2(w,v,index+1,rest-w[index],path[:]+[v[index]],res)
    return

w = [2,3,4,5]
v = [1,2,5,7]
index = 0
rest = 8
path = []
res = []
bag_digui2(w,v,index,rest,path,res)
print(max(res ))
