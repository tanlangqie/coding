# -*- coding: utf-8 -*-#

# Name:   coding_input.py
# Author: tangzhuang
# Date:   2021/7/11
# desc:         

"""
刷题，自己写输入
"""
#单个数
# n = input().strip()
# n = int(n)
# #一维数组
# arr = input().strip().split(" ")
# arr =[ int(i) for i in arr]
# #题目要求n行输入(n不是固定的)
# arr=[]
# n = input().strip()
# n = int(n)
# for _ in range(n):
#     x1,x2,x3,x4 = input().strip().split(" ")
#     arr.append([int(x1),int(x2),int(x3),int(x4)])
# print(arr)
#
# #牛客网输入
# import sys
# m = sys.stdin.readline().strip().split()
# card = sys.stdin.readline().strip()
#
# # 导入 random(随机数) 模块
# import random
# print(random.randint(0, 9))


# a,b = map(int,input().strip().split())
# print(a,b)
# arr = list(map(int,list(input().strip().split())))
# print(arr)

a = [1,4,2]
ss = sorted(a)
print(ss)