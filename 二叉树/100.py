# -*- coding: utf-8 -*-#

# Name:   100.py
# Author: tangzhuang
# Date:   2021/7/20
# desc: 判断两棵树是否相等

def isSameTree(self, s, t):
    if not s and not t:  # 递归出口
        return True
    if not s or not t:
        return False
    return s.val == t.val and self.isSameTree(s.left, t.left) and self.isSameTree(s.right, t.right)



