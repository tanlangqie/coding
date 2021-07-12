# -*- coding: utf-8 -*-#

# Name:   删除排序数组中的重复项.py
# Author: tangzhuang
# Date:   2021/7/12
# desc:         


# 双指针，fast寻找第一个不重复值得位置；low指针指向需要被替换的位置，替换后low+=1
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0

        n = len(nums)
        fast = slow = 1
        while fast < n:
            if nums[fast] != nums[fast - 1]:
                nums[slow] = nums[fast]
                slow += 1
            fast += 1

        return slow

# https://leetcode-cn.com/problems/remove-duplicates-from-sorted-array/solution/shan-chu-pai-xu-shu-zu-zhong-de-zhong-fu-tudo/