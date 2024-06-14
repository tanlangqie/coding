# -*- coding: utf-8 -*-#

# Name:   背包问题.py
# Author: tangzhuang
# Date:   2021/3/27
# desc:   有很多种可能，要遍历尝试所有的可能---》递归  (从左到右)递归




#递归求解
# w 代表物品的重量
# v 代表物品的价值

#
# #初版递归，递归函数不返回目标值，递归函数只是遍历一遍所有可能，由path记录路径，res统计每条路径对应的目标 结果，在递归函数的外层在去处理res的结果
# def bag_digui2(w,v,index,rest,path,res):
#
#     #base case 1
#     if rest <= 0:
#         res.append(sum(path))
#         return
#     #base case 2
#     if index == len(w):
#         res.append(sum(path))
#         return
#
#     #不要第i个物品
#     bag_digui2(w,v,index+1,rest,path[:],res)
#
#     #要第i个物品
#     p2 = -1
#     if rest >= w[index]:
#         bag_digui2(w,v,index+1,rest-w[index],path[:]+[v[index]],res)
#     return
#
# w = [2,3,4,5]
# v = [1,2,5,7]
# index = 0
# rest = 8
# path = []
# res = []
# bag_digui2(w,v,index,rest,path,res)
# print(max(res ))


#优化 后的递归，不需要path与res了，递归函数直接返回目标值。
#走到第index步，只剩下rest的空间了.后面一截能获得的最大值
def bag_digui(w,v,index,rest):

    #base case 1  没有空间剩余了
    if rest <= 0:
        return 0
    #base case 2   有空间剩余，但是没货物了
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
    #dp[i,j]代表走到第i个物品，还剩余j的空间时，能获得的最大的价值
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


# 二维数组
#     w = [2,3,4,5]
#     v = [1,2,5,7]
import numpy as np
#dp[i][j] 走到第i个物品有j个空间容量时，最大能装多少东西
def solve(vlist,wlist,totalWeight,totalLength):
    resArr = np.zeros((totalLength+1,totalWeight+1),dtype=np.int32)
    for i in range(1,totalLength+1):                 #物品
        for j in range(1,totalWeight+1):               # 背包容量
            if wlist[i-1] <= j:
                resArr[i,j] = max(resArr[i-1,j-wlist[i-1]]+vlist[i-1],resArr[i-1,j])
            else:
                resArr[i,j] = resArr[i-1,j]
    print(resArr)
    return resArr[-1,-1]

"""

#一维解法
# n, v分别代表物品数量，背包容积
n, v = map(int, input().split())
# w为物品价值，c为物品体积（花费）
w, cost = [0], [0]
for i in range(n):
    cur_c, cur_w = map(int, input().split())
    w.append(cur_w)
    cost.append(cur_c)

#该初始化代表背包不一定要装满
dp = [0 for j in range(v+1)]

for i in range(1, n+1):
    #注意：第二层循环要逆序循环
    for j in range(v, 0, -1):       #可优化成 for j in range(v, cost[i]-1, -1): 
        if j >= cost[i]:
            dp[j] = max(dp[j], dp[j-cost[i]]+w[i])

print(dp[v])

https://zhuanlan.zhihu.com/p/136179953
"""






if __name__ == '__main__':
    w = [2,3,4,5]
    v = [1,2,5,7]
    index = 0
    rest = 8
    # res = bag_digui(w,v,index,rest)
    # print(res )
    #
    # a,b = bag_dp(w,v,rest)
    # print(a)
    # print(b)

    ss = solve(v, w, rest, 4)
    print(ss)
    # for i in range(3, -1,-1):
    #     print(i)


############# 背包9解开  ##############
"""
https://leetcode-cn.com/problems/partition-equal-subset-sum/solution/yi-tao-kuang-jia-jie-jue-bei-bao-wen-ti-p9saf/
"""


"""

背包问题解法：
01 背包问题：
如果是 01 背包，即数组中的元素不可重复使用，外循环遍历 arrs，内循环遍历 target，且内循环倒序:

完全背包问题：
（1）如果是完全背包，即数组中的元素可重复使用并且不考虑元素之间顺序，arrs 放在外循环（保证 arrs 按顺序），target在内循环。且内循环正序。
（2）如果组合问题需考虑元素之间的顺序，需将 target 放在外循环，将 arrs 放在内循环，且内循环正序。

作者：wulafly-2
链接：https://leetcode-cn.com/problems/partition-equal-subset-sum/solution/yi-tao-kuang-jia-jie-jue-bei-bao-wen-ti-p9saf/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

"""