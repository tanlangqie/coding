'''

你是一个专业的小偷，计划偷窃沿街的房屋。每间房内都藏有一定的现金，影响你偷窃的唯一制约因素就是相邻的房屋装有相互连通的防盗系统，
如果两间相邻的房屋在同一晚上被小偷闯入，系统会自动报警。

给定一个代表每个房屋存放金额的非负整数数组，计算你在不触动警报装置的情况下，能够偷窃到的最高金额。
题目：https://leetcode-cn.com/problems/house-robber/
'''

#暴力递归版本
class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]

        def fun(i, nums, path, res):
            if i >= len(nums):
                res.append(sum(path))
                return
            # 要第i个
            fun(i + 2, nums, path + [nums[i]], res)
            # 不要第i个
            fun(i + 1, nums, path, res)
            return

        path = []
        res = []
        fun(0, nums, path, res)
        return max(res)

# 暴力递归 ---直接返回最大值
class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]

        def fun(i, nums, path, res):
            if i >= len(nums):
                return max(sum(path), res)
            # 要第i个

            t = fun(i + 2, nums, path + [nums[i]], res)
            # 不要第i个
            t1 = fun(i + 1, nums, path, res)
            return max(t, t1)

        path = []
        res = -float('inf')

        return fun(0, nums, path, res)























class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums)

        fn = [nums[0], max(nums[0], nums[1])]
        # res = 0
        for i in range(2, len(nums)):
            fn.append(max(fn[i - 1], fn[i - 2] + nums[i]))
        return max(fn)




