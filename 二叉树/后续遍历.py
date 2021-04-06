# -*- coding: utf-8 -*-#

# Name:         后续遍历.py
# Description:
# Author:       tangzhuang
# Date:         2021/3/3
# desc:     根-》右--》左      翻转    左--》右--》根

def fun(root):
    res = []
    if not root:
        return []
    s = [root]
    while s:
        n = s.pop()
        res.append(n.val)

        if n.left :
            s.append(n.left)
        if n.right:
           s.append(n.right)
    res.reverse()
    return res