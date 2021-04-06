# -*- coding: utf-8 -*-#

#题目：给定一个整数arr，代表数值不同的纸牌排成一条线，玩家A先拿，玩家b后拿，每次都只能拿走最左或者最右的纸牌
#谁的分数大，谁获胜，返回获胜者的分数

# Name:   两个人最大得分.py
# Author: tangzhuang
# Date:   2021/3/27
# desc:   要尝试-遍历每一种可---》递归---》左边拿或者右边拿---》范围上的递归尝试


def win(arr):
    if arr == None or len(arr)==0:
        return  0
    return max(f(arr,0,len(arr)-1),s(arr,0,len(arr)-1))

#先手函数
def f(arr,l,r):
    if l == r:
        return arr[l]
    return max(arr[l]+s(arr,l+1,r),arr[r]+s(arr,l,r-1))

#后手函数
def s(arr,l,r):
    if l == r:
        return 0
    return min(f(arr,l+1,r),f(arr,l,r-1))


if __name__ == '__main__':
    arr = [1,10,5]
    res = win(arr)
    print(res)