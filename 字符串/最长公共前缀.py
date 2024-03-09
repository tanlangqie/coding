# -*- coding: utf-8 -*-#

# Name:   最长公共前缀.py
# Author: tangzhuang
# Date:   2021/7/12
# 编写一个函数来查找字符串数组中的最长公共前缀。如果不存在公共前缀，返回空字符串
# 输入：strs = ["flower","flow","flight"]
# 输出："fl"
# desc:    https://leetcode-cn.com/problems/longest-common-prefix/solution/zui-chang-gong-gong-qian-zhui-by-leetcode-solution/



#水平扫描，计算第一个字符串与第二个字符串的最长公共子序列(tem_str)，用得到的tem_str与
#第3个字符串放在一起，求最长公共子序列，并更新tem_str，依次遍历整个数组

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""

        prefix, count = strs[0], len(strs)
        for i in range(1, count):
            prefix = self.lcp(prefix, strs[i])
            if not prefix:
                break

        return prefix

    def lcp(self, str1, str2):
        length, index = min(len(str1), len(str2)), 0
        while index < length and str1[index] == str2[index]:
            index += 1
        return str1[:index]


# 作者：LeetCode - Solution
# 链接：https: // leetcode - cn.com / problems / longest - common - prefix / solution / zui - chang - gong - gong - qian - zhui - by - leetcode - solution /
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。





# 分治法，递归...   递归函数定义为求一个字符串序列的公共子序列
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        def lcp(start, end):
            if start == end:
                return strs[start]

            mid = (start + end) // 2
            lcpLeft, lcpRight = lcp(start, mid), lcp(mid + 1, end)
            minLength = min(len(lcpLeft), len(lcpRight))
            for i in range(minLength):
                if lcpLeft[i] != lcpRight[i]:
                    return lcpLeft[:i]

            return lcpLeft[:minLength]

        return "" if not strs else lcp(0, len(strs) - 1)

# 作者：LeetCode-Solution
# 链接：https://leetcode-cn.com/problems/longest-common-prefix/solution/zui-chang-gong-gong-qian-zhui-by-leetcode-solution/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
