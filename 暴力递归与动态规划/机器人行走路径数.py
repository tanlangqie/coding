# -*- coding: utf-8 -*-#
#题目：一个机器人在一个m*n的棋盘上，从左上角走到右下角一共有几条路径
# Name:   机器人行走路径数.py
# Author: tangzhuang
# Date:   2021/3/27
# desc:     力扣原题：https://leetcode-cn.com/problems/unique-paths/submissions/

###暴力递归
class Solution:

    def uniquePaths(self, m: int, n: int) -> int:
        i = 1
        j = 1

        def fun(i,j,m,n):
            res = 0
            if i == m and j == n:
                return 1
            if i + 1 <= m and j <=n:
                res +=fun(i+1,j,m,n)
            if j + 1 <= n and i <= m:
                res +=fun(i,j+1,m,n)
            return res

        return fun(1,1,m,n)



###############动态规划
import numpy as np
#
# def uniquePaths(m,n):
#     dp = [[0 for i in range(n)] for j in range(m)]
#     dp = np.array(dp)
#     dp[:, 0] = 1
#     dp[0, :] = 1
#     for i in range(1, m):
#         for j in range(1, n):
#             dp[i, j] = dp[i - 1, j] + dp[i, j - 1]
#     return dp[-1, -1]
# print(uniquePaths(3,7))


##############动态规划--优化空间复杂度
"""
 使用二维数组的时候，dp[i][j] = dp[i-1][j] + dp[i][j-1] ，每一个格子的数据等于上面一个格子加左边格子的数据。
 可以想象一下，计算一行数据的时候，直接把上面一行的数据搬下来，然后每个格子就等于前一个格子的数据加上当前格子的数据。
"""
def uniquePaths(m,n):
    cur = [1] * n
    for i in range(1, m):
        for j in range(1, n):
            cur[j] += cur[j - 1]
            print(cur)
    return cur[-1]
uniquePaths(3,7)