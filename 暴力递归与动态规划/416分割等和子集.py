# -*- coding: utf-8 -*-#

# Name:   416分割等和子集.py
# Author: tangzhuang
# Date:   2021/7/6
# desc:     给你一个 只包含正整数 的 非空 数组 nums 。请你判断是否可以将这个数组分割成两个子集，使得两个子集的元素和相等。
# https://leetcode-cn.com/problems/partition-equal-subset-sum/

#暴力递归--ok
def canPartition(nums ):
    res = sum(nums)
    if len(nums)<2:
        return False
    num = 0
    def help(nums,i,num,res):
        if num * 2 == res:
            return True
        if i < len(nums):
            a = help(nums,i+1,num,res)
            b = help(nums,i+1,num+nums[i],res)
            return a or b
        else:
            return False
    return help(nums,0,num,res)


#动态规划
# 创建二维数组 dp，包含 n 行target+1 列，其中 dp[i][j] 表示从数组的[0,i]
#  下标范围内选取若干个正整数（可以是 0 个），是否存在一种选取方案使得被选取的正整数的和等于 j。初始时，dp 中的全部元素都是
# false。

 
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        if n < 2:
            return False

        total = sum(nums)
        maxNum = max(nums)
        if total & 1:
            return False

        target = total // 2
        if maxNum > target:
            return False

        dp = [[0] * (target + 1) for _ in range(n)]
        for i in range(n):
            dp[i][0] = True

        dp[0][nums[0]] = True
        for i in range(1, n):
            num = nums[i]
            for j in range(1, target + 1):
                if j >= num:
                    dp[i][j] = dp[i - 1][j] | dp[i - 1][j - num]
                else:
                    dp[i][j] = dp[i - 1][j]

        return dp[n - 1][target]


# 作者：LeetCode - Solution
# 链接：https: // leetcode - cn.com / problems / partition - equal - subset - sum / solution / fen - ge - deng - he - zi - ji - by - leetcode - solution /
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。