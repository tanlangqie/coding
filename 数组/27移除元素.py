# -*- coding: utf-8 -*-#

# Name:   27移除元素.py
# Author: tangzhuang
# Date:   2021/7/17
# desc:   原地删除数组中值为 val的元素， 时间O(n),空间O(1)

class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        k = 0   #满足条件的索引
        for i in range(len(nums)):
            if(nums[i]!=val):    #找到不等于制定值的索引进行赋值
                nums[k] = nums[i]
                k += 1
        return k

# # 快慢指针，step1:找到两个指针的起始位置；step2:快指针的值满足条件后就赋值给慢指针，然后low+1
# class Solution:
#     def removeElement(self, nums: List[int], val: int) -> int:
#         size = len(nums)
#         if size == 0:
#             return 0
#
#         low, fast = 0, 0
#         while fast < size:
#             if nums[fast] != val:
#                 break
#             fast += 1
#
#         while fast < size:
#             if nums[fast] != val:
#                 nums[low] = nums[fast]
#                 low += 1
#             fast += 1
#         return low




