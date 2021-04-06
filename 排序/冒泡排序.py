# -*- coding: utf-8 -*-#

# Name:         冒泡排序.py
# Description:
# Author:       tangzhuang
# Date:         2021/2/27
# Desc:      冒泡排序，依次比较相邻的两个数字，大的放在右边

def maopao():
    # a = [7,6,5,8,1,3,2,9,4]
    a = [1,2,3,4,5,6,7,8,9]
    for i in range(len(a)-1):
        flag = 0
        for j in range(len(a)-i-1):
            if a[j] > a[j+1]:
                a[j],a[j+1] = a[j+1],a[j]
                flag = 1
        if  flag:
            return  a
    print(a)

maopao()