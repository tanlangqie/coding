# -*- coding: utf-8 -*-#

# Name:         后序遍历.py
# Description:
# Author:       tangzhuang
# Date:         2021/3/3
# desc:     根-》右--》左      翻转    左--》右--》根






# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right



class Solution:
    def postorderTraversal(self, root):
        def postorder(root):
            if not root:
                return
            postorder(root.left)
            postorder(root.right)
            res.append(root.val)

        res = list()
        postorder(root)
        return res



#非递归，先根-》左-》右入栈，然后在反序输出
class Solution:
    def postorderTraversal(self, root):
        if root is None:
            return []
        s = []
        s.append(root)
        res = []
        while s:
            node = s.pop()
            res.append(node.val)
            if node.left:
                s.append(node.left)
            if node.right:
                s.append(node.right)

        return res[::-1]





# 非递归
# def fun(root):
#     res = []
#     if not root:
#         return []
#     s = [root]
#     while s:
#         n = s.pop()
#         res.append(n.val)
#
#         if n.left :
#             s.append(n.left)
#         if n.right:
#            s.append(n.right)
#     res.reverse()
#     return res