# -*- coding: utf-8 -*-#

# Name:         前序遍历.py
# Description:
# Author:       tangzhuang
# Date:         2021/3/2
# desc:         二叉树的前序遍历, 非递归就用栈处理

# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#递归    返回树的前序列
def fun(root):
    res = []
    if not root:
        return []

    res.append(root.val)
    res += fun(root.left)
    res += fun(root.right)
    return res


#非递归    用栈处理。。。根->右->左的形式压栈
class Solution:
    def preorderTraversal(self, root):
        if root is None:
            return []
        s = []
        s.append(root)
        res = []
        while s:
            node = s.pop()
            res.append(node.val)
            if node.right:
                s.append(node.right)
            if node.left:
                s.append(node.left)
        return res


def qian(root):
    if root is None:
        return []
    s = []
    res = []
    s.append(root)
    while s:
        t = s.pop()
        res.append(t.val)
        if t.right:
            t.append(t.right)
        if t.left:
            s.append(t.left)
    return


def hou(root):
    if root is None:
        return []
    s = []
    res = []
    s.append(root)
    while s:
        t = s.pop()
        res.append(t.val)
        if t.left:
            s.append(t.left)
        if t.right:
            t.append(t.right)

    return res[::-1]


def zhong(root):
    if root is None:
        return []
    s = []
    res = []
    while s or root:
        if root:
            s.append(root)
            root = root.left
        else:
            root = s.pop()
            res.append(root.val)
            root=root.right

    return res