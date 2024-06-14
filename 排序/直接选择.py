# -*- coding: utf-8 -*-#

# Name:         直接选择排序.py
# Description:
# Author:       tangzhuang
# Date:         2021/2/27
# Desc:      直接选择排序，每次选择最小的放在最左边




def change():
    a = [7,6,5,8,1,3,2,9,4]
    # a = [1,2,3,4,5,6,7,8,9]
    for i in range(len(a)-1):
        min = i
        for j in range(i,len(a)):
            if a[j] < a[min]:
                min = j
        a[min],a[i] = a[i],a[min]

    print(a)

change()


