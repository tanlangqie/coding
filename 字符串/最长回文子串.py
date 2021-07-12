# -*- coding: utf-8 -*-#

# Name:   5最长回文子串.py
# Author: tangzhuang
# Date:   2021/7/12
# desc:
# 输入：s = "babad"
# 输出："bab"
# 解释："aba" 同样是符合题意的答案。

class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        res = ""
        if len(s) < 2:
            return s

        length = len(s)
        for i in range(0, length):
            left = i
            right = i + 1
            while left > -1 and right < length and s[left] == s[right]:
                left -= 1
                right += 1
            if right - left - 1 > len(res):
                res = s[left + 1:right]

            left1 = i
            right1 = i
            while left1 > -1 and right1 < length and s[left1] == s[right1]:
                left1 -= 1
                right1 += 1
            if right1 - left1 - 1 > len(res):
                res = s[left1 + 1:right1]
        return res
