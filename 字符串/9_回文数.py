# -*- coding: utf-8 -*-#

# Name:   9_回文数.py
# Author: tangzhuang
# Date:   2024/4/2
# desc:         

"""
给你一个整数 x ，如果 x 是一个回文整数，返回 true ；否则，返回 false 。

回文数
是指正序（从左向右）和倒序（从右向左）读都是一样的整数。

例如，121 是回文，而 123 不是。
 

示例 1：

输入：x = 121
输出：true
示例 2：

输入：x = -121
输出：false
解释：从左向右读, 为 -121 。 从右向左读, 为 121- 。因此它不是一个回文数。
"""

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        x=list(str(x))
        for i in range(len(x)):
            if x[i] != x[::-1][i]:
                return False
        return True