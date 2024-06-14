'''
题目：https://leetcode-cn.com/problems/maximum-subarray/
给定一个整数数组 nums ，找到一个具有最大和的连续子数组
（子数组最少包含一个元素），返回其最大和。

动态规划
1.定义一个函数f(n)，以第n个数为结束点的子数列的最大和，存在一个递推关系f(n) = max(f(n-1) + A[n], A[n]);
2.将这些最大和保存下来后，取最大的那个就是，最大子数组和。因为最大连续子数组 等价于 最大的以n个数为结束点的子数列和 附代码
'''
class Solution:
    def maxSubArray(self, nums) :
        if len(nums) < 1:
            return None
        res = nums[0]
        f_n = nums[0]
        for i in range(1,len(nums)):
            f_n = max(f_n + nums[i],nums[i])
            res = max(res,f_n)
        return res
a = Solution()
print(a.maxSubArray([1,2,-4,5,7]))



'''
这个方法的fn是保存在list中的，上个方法的fn是只保存当前第i步的fn值

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums)<1:
            return 0
        fn = [nums[0]]
        for i in range(1,len(nums)):
            tem = max(fn[i-1] + nums[i], nums[i])
            fn.append(tem)
        return max(fn)


'''
def fun(arr):
    size = len(arr)
    dp = [0] * size
    dp[0] = max(0,arr[0])
    for i in range(1,size):
        dp[i] = max(dp[i-1]+arr[i],arr[i])
    print(max(dp))
    print(dp)
fun([1,5,-10,2,5,-3,2,6,-3,1])




"""
暴力递归
    def maxSubArray(self, nums: List[int]) -> int:
        
        if len(nums)==0:
            return None
        if len(nums)==1:
            return nums[0]
        path = nums[0]
        i = 1
        res = [] 
        #走到第i步的最大值
        def fun(i,nums,path,res):
            res.append(path)
            if i == len(nums):
                return path
            return fun(i+1,nums,max(nums[i],path+nums[i]),res)
        fun(i,nums,path,res)
        return max(res)



"""

#20240329---出错了
def fun(nums):
    if len(nums) < 1:
        return None
    res = nums[0]
    for i in range(1, len(nums)):
        res = max(res+nums[i],nums[i])   #错误原因：这里的res其实记录的是第i个位置的最大值dp[i]，并不是最终结果的最大值，应该在用一个res来求dp[i]的最值
    return res