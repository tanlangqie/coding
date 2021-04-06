# -*- coding: utf-8 -*-#

# Name:         前序遍历.py
# Description:
# Author:       tangzhuang
# Date:         2021/3/2
# desc:         二叉树的前序遍历



#递归
def fun(root):
    res = []
    if not root:
        return []

    res.append(root.val)
    res += fun(root.left)
    res += fun(root.right)
    return res


#非递归
def fun(root):
    res = []
    if not root:
        return  []
    s = []

    while s  or root:
        if root:
            s.append(root)
            res.append(root.val)
            root = root.left
        else:
            root= s.pop()
            root = root.right
    return res

