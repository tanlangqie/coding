# -*- coding: utf-8 -*-#

# Name:         希尔排序.py
# Description:
# Author:       tangzhuang
# Date:         2021/2/28
# desc:         带间隔的插入排序，每个子序列内部都是用插入排序，时间复杂度o 1.3,空间复杂度o(1). 不稳定

#
def shell():
    a = [5,7,12,3,9,8,10,1,9,13,6,15,4,11,2]
    gape = 4
    while gape > 0:
        for i in range(gape,len(a)):
            k = i
            while k > gape-1:
                if a[k] < a[k-gape]:
                    a[k],a[k-gape] = a[k-gape],a[k]
                k -= gape
        gape /=2
        gape = int(gape)

    print(a)

shell()


# for k in range(4,3,4):
#     print(k)