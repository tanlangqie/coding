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


输入：nums = [3,2,1,0,4]
输出：false
解释：无论怎样，总会到达下标为 3 的位置。但该下标的最大跳跃长度是 0 ， 所以永远不可能到达最后一个下标。
"""


# 最远的距离由index和该index上的值决定。。   注意当 i<=max_l 代表能到达，才可以比较
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        size = len(nums)
        max_l = 0    #最开始假象有个光标在数组的-1处，此时能走的最远距离是0，现在准备往右遍历了
        for i in range(size-1):
            if max_l >= i:  #防止【0-2-3】这种用例，从0开始都没机会到达下一个
                max_l = max(max_l,i+nums[i])    #动态规划方程：到当前位置的最大值为之前的最大值或者当前位置加上当前位置的数组值
        if max_l >= size-1:
            return True
        return False


# 20240329 x
def fun(nums):
    if nums is None:
        return False
    max_step = nums[0]
    for i in range(len(nums)-1):
        max_step = max(i+nums[i],max_step)
    if max_step>=len(nums)-1:
        return True
    return False

# 20240414 基于跳跃游戏2改版。只需要在结尾处加个判断就可以
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if nums is None:
            return False
        n = len(nums)
        maxPos, end, step = 0, 0, 0
        for i in range(n - 1):
            if maxPos >= i:
                maxPos = max(maxPos, i + nums[i])
                if i == end:
                    end = maxPos
                    step += 1

        if maxPos>=len(nums)-1:
            return True
        return False