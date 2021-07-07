# -*- coding: utf-8 -*-#

# Name:         层序遍历.py
# Description:
# Author:       tangzhuang
# Date:         2021/3/3
# desc:        先进先出   队列

def fun(root):
    res = []
    if not root:
        return  []
    q = [root]
    while len(q):
        tem = []
        for i in range(len(1)):
            a = q.pop(0)
            tem.append(a.val)
            if a.left:
                q.append(a.left)
            if a.right:
                q.append(a.right)
        res.qppend(tem)
    return  res

def f(root):
    res = []
    q = []
    q.append(root)
    while len(q):
        tem = []
        for i in range(len(q)):
            a = q.pop(0)
