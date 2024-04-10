# -*- coding: utf-8 -*-#

# Name:   46_全排列.py
# Author: tangzhuang
# Date:   2024/3/31
# desc:         

"""

给定一个不含重复数字的数组 nums ，返回其 所有可能的全排列 。你可以 按任意顺序 返回答案。


示例 1：

输入：nums = [1,2,3]
输出：[[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
示例 2：

输入：nums = [0,1]
输出：[[0,1],[1,0]]
示例 3：

输入：nums = [1]
输出：[[1]]
"""


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums)==0:
            return None
        path = []
        res = []
        def fun(nums,path,res):
            if len(nums) == 0:
                res.append(path)
                return
            for i in range(len(nums)):
                fun(nums[:i]+nums[i+1:],path+[nums[i]],res)
        fun(nums,path,res)
        return res