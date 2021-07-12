# -*- coding: utf-8 -*-#

# Name:   二叉树子树问题.py
# Author: tangzhuang
# Date:   2021/7/9
# desc:  leetcode 572   一个树是另一个树的子树

class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        if not s and not t:  # 均为空   递归出口
            return True
        if not s or not t:  # 有一个非空
            return False
        return self.isSameTree(s, t) or self.isSubtree(s.left, t) or self.isSubtree(s.right, t)

    def isSameTree(self, s, t):
        if not s and not t:  # 递归出口
            return True
        if not s or not t:
            return False
        return s.val == t.val and self.isSameTree(s.left, t.left) and self.isSameTree(s.right, t.right)


# 原文链接：https: // blog.csdn.net / weixin_41888257 / article / details / 107131346
def is_sub(s,t):
    if s is None and t is None:
        return  True
    if not s or not t :
        return False
    return is_equ(s,t) or is_equ(s.left,t) or is_equ(s.right,t)

def is_equ():
