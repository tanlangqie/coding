# -*- coding: utf-8 -*-#

# Name:   20_有效括号.py
# Author: tangzhuang
# Date:   2024/4/7
# desc:         https://leetcode.cn/problems/valid-parentheses/description/

"""
给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串 s ，判断字符串是否有效。

有效字符串需满足：

左括号必须用相同类型的右括号闭合。
左括号必须以正确的顺序闭合。
每个右括号都有一个对应的相同类型的左括号。
 

示例 1：

输入：s = "()"
输出：true
示例 2：

输入：s = "()[]{}"
输出：true
示例 3：

输入：s = "(]"
输出：false

"""


# 用栈
# 括号都是匹配的，用字典定义一个括号匹配规则。
# 依次遍历字符串，用栈记录左括号，当出现右括号后判断其是否与栈顶元素匹配，  匹配就继续遍历下一个，否则就返回false
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        dic = {')':'(','}':'{',']':'['}
        if len(s) == 1:
            return False
        if len(s) == 0:
            return True
        stack = []
        for i in s:
            if i not in dic:
                stack.append(i)
            else:
                if len(stack)<1 or stack.pop() != dic[i]:
                    return False
        return True if len(stack)== 0 else False
