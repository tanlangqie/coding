# -*- coding: utf-8 -*-#

# Name:         插入排序.py
# Description:
# Author:       tangzhuang
# Date:         2021/2/27
# desc:   类似打牌，认为左边的有序（最开始是第一个有序），将右边的一个插入到左边合适的位置. 外层for循环只控制 循环次数，内层的循环才涉及到数组值比较



# 易错点，外层循环从第一个开始的；内层循环从i开始降序
#内层循环 j 与 j-1进行对比

def insert():
    a = [5,3,4,9,8,6,7,2,1]

    for i in range(1,len(a)):
        for j in range(i,0,-1):
            if a[j] < a[j-1]:
                a[j],a[j-1] = a[j-1],a[j]

    print(a)
insert()


