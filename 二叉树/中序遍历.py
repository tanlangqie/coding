# -*- coding: utf-8 -*-#

# Name:         中序遍历.py
# Description:
# Author:       tangzhuang
# Date:         2021/3/2
# desc:         二叉树的中序遍历


def fun(root):
    res = []
    if not root:
        return []
    s = []
    while s or root:
        if root :
            s.append(root)
            root = root.left
        else:
            root = s.pop()
            res.append(root.val)
            root = root.right

