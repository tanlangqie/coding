# -*- coding: utf-8 -*-#

# Name:   55跳跃游戏1.py
# Author: tangzhuang
# Date:   2021/7/18
# desc:         

"""
给定一个非负整数数组 nums ，你最初位于数组的 第一个下标 。

数组中的每个元素代表你在该位置可以跳跃的最大长度。

判断你是否能够到达最后一个下标。

 

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/jump-game
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。


输入：nums = [2,3,1,1,4]
输出：true
解释：可以先跳 1 步，从下标 0 到达下标 1, 然后再从下标 1 跳 3 步到达最后一个下标。
"""


# 最远的距离由index和该index上的值决定。。   注意当 i<=max_l 代表能到达，才可以比较
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        size = len(nums)
        max_l = 0
        for i in range(size-1):
            if max_l >= i:
                max_l = max(max_l,i+nums[i])
        if max_l >= size-1:
            return True
        return False