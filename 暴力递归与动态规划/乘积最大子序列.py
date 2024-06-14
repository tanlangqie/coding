'''
0

给定一个整数数组 nums ，找出一个序列中乘积最大的连续子序列（该序列至少包含一个数）。

输入: [2,3,-2,4]输出: 6解释: 子数组 [2,3] 有最大乘积 6。

因为负数乘于一个负数可以可以变成正书，所以要记录最小值和最大值
我们只要记录前i的最小值, 和最大值, 那么以第i个位置结尾的最大值dp[i] = max(nums[i] * pre_max, nums[i] * pre_min, nums[i]), 这里0 不需要单独考虑, 因为当相乘不管最大值和最小值,都会置0
注意在记录最大值的过程中，因为最大值和最小值会互相影响，所以要用临时变量
作者：powcai
链接：https://leetcode-cn.com/problems/two-sum/solution/duo-chong-si-lu-qiu-jie-by-powcai-3/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
'''

# class Solution:
#     def maxProduct(self, nums: List[int]) -> int:
#         if not nums: return
#         res = nums[0]
#         pre_max = nums[0]
#         pre_min = nums[0]
#         for num in nums[1:]:
#             cur_max = max(pre_max * num, pre_min * num, num)
#             cur_min = min(pre_max * num, pre_min * num, num)
#             res = max(res, cur_max)
#             pre_max = cur_max
#             pre_min = cur_min
#         return res

# 作者：powcai
# 链接：https://leetcode-cn.com/problems/two-sum/solution/duo-chong-si-lu-qiu-jie-by-powcai-3/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。


#20240329------出错了 ，pre_max的值会影响pre_min的值，因此需要中间遍历来处理
class Solution:
    def maxProduct(self, nums )  :
        if not nums: return
        if not nums: return
        res = [nums[0]]
        pre_max = nums[0]
        pre_min = nums[0]
        for num in nums[1:]:
            res.append(max(pre_max * num, pre_min * num, num))  #存放结果
            pre_max = max(pre_max * num, pre_min * num, num)    #dp[i]
            pre_min = min(pre_max * num, pre_min * num, num)
        return max(res)
s = Solution()
nums = [-4,-3,-2]
res = s.maxProduct(nums)
print(res)