# -*- coding: utf-8 -*-#

# Name:   背包问题.py
# Author: tangzhuang
# Date:   2021/3/27
# desc:   有很多种可能，要遍历尝试所有的可能---》递归  (从左到右)递归




#递归求解
# w 代表物品的重量
# v 代表物品的价值

#走到第index步，只剩下rest的空间了.能获得的最大值
def bag_digui(w,v,index,rest):

    #base case 1
    if rest <= 0:
        return 0
    #base case 2
    if index == len(w):
        return  0

    #不要第i个物品
    p1 = bag_digui(w,v,index+1,rest)

    #要第i个物品
    p2 = -1
    if rest >= w[index]:
        p2 = v[index] + bag_digui(w,v,index+1,rest-w[index])


    return  max(p1,p2)



#动态规划解法

def bag_dp(w,v,rest):
    import numpy as np
    n = len(w)
    #dp[i,j]代表走到第i个物品，还剩余j的空间时，最大的价值
    dp = np.zeros((n + 1, rest + 1))

    # dp[n,:] = 0
    for i in range(n-1, -1,-1):
        for j in range(rest+1):
            #当不要第i个物品时，能获得的最大的价值和从i+1位置看是一样的
            p1 = dp[i+1][j]
            p2 = -1
            #当剩余空间足够时，要第i个物品
            if j - w[i] >=0:
                p2 = v[i] + dp[i+1,j-w[i]]

            dp[i,j] = max(p1,p2)

    return dp[0,rest],dp










if __name__ == '__main__':
    w = [2,3,4,5]
    v = [1,2,5,7]
    index = 0
    rest = 8
    res = bag_digui(w,v,index,rest)
    print(res )

    a,b = bag_dp(w,v,rest)
    print(a)
    print(b)


    # for i in range(3, -1,-1):
    #     print(i)