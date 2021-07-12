# -*- coding: utf-8 -*-#

# Name:   无重复字符的最长子串.py
# Author: tangzhuang
# Date:   2021/7/11
# desc:       给定一个字符串 s ，请你找出其中不含有重复字符的 最长子串 的长度。


# 双指针（滑动窗口）----》star为滑动窗口的左指针
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        dic = {}
        start, maxlen, substr = 0, 0, ""

        for i, x in enumerate(s):
            if x in dic:
                start = max(dic[x] + 1, start)   #
                dic[x] = i
            else:
                dic[x] = i

            if i - start + 1 > maxlen:
                maxlen = i - start + 1
                substr = s[start:i + 1]
        return maxlen




        # 作者：powcai
        # 链接：https://leetcode-cn.com/problems/two-sum/solution/hua-dong-chuang-kou-by-powcai/
        # 来源：力扣（LeetCode）
        # 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。