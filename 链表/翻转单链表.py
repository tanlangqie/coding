# -*- coding: utf-8 -*-#

# Name:         翻转单链表.py
# Description:
# Author:       tangzhuang
# Date:         2021/3/3
# desc:         

def fun(phead):
    if phead == None or phead.next == None:
        return  phead
    thead = None
    p = phead
    while p:
        n = p.next
        p.next = thead
        thead = p
        p = n
    return p
