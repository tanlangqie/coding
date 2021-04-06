# -*- coding: utf-8 -*-#

# Name:         quick_sort.py
# Description:
# Author:       tangzhuang
# Date:         2021/3/1
# desc:         快速排序


def quick_sort(a,low,high):

    i = low
    j =high
    tem = a [i]
    while i<j:
        while i < j and a[j] >= tem:
            j -= 1
        if i <j:
            a[i] = a[j]
            i += 1

        while i < j and a[i]<=tem:
            i += 1
        if i <j:
            a[j] = a[i]
            j -= 1

    a[i] = tem

    if low < i:
        quick_sort(a,low,i-1)
    if i < high:
        quick_sort(a, j+1, high)

    return  a


# 易错点
#1.有两个while
#2.第2个while的判断条件中有等号
#3.递归之前也有条件判断,判断索引边界
#4.每次递归的tem是取arr[low]，而不是arr[0]
def fun(a,l,r):
    i = l
    j = r
    tem = a[i]
    while i<j:
        while i<j and a[j]>=tem:
            j -= 1
        if i < j:
            a[i] = a[j]
            i += 1
        while i < j and a[i]<=tem:
            i += 1
        if i < j:
            a[j] = a[i]
            j -= 1
    a[i] = tem
    if l < i:
        fun(a,l,i-1)
    if r > i:
        fun(a,i+1,r)

    return a

a = [5,7,1,3,9,6,2,4,8]
# res = quick_sort(a,0,8)
res = fun(a,0,8)

print(res)