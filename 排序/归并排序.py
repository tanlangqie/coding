# -*- coding: utf-8 -*-#

# Name:         归并排序.py
# Description:
# Author:       tangzhuang
# Date:         2021/2/28
# desc:         先递归拆分，再两两合并

def merge(a,b):
    #
    res = []
    i = 0
    j = 0
    while i<len(a) and j<len(b):
        if a[i] <= b[j]:
            res.append(a[i])
            i += 1
        else:
            res.append(b[j])
            j += 1
    if i == len(a):
        res.extend(b[j:])
    if j == len(b):
        res.extend(a[i:])
    return  res


def sort(t):
    if len(t) < 2:
        return  t
    half = len(t)//2
    l = sort(t[:half])
    r = sort(t[half:])
    return merge(l,r)

a = [5,7,12,3,9,8,10,1,9,13,6,15,4,11,2]
res = sort(a)
print(res)