# -*- coding: utf-8 -*-#

# Name:         翻转单链表.py
# Description:
# Author:       tangzhuang
# Date:         2021/3/3
# desc:         

def fun(phead):
    if phead == None or phead.next == None:
        return  phead
    pre = None
    cur = phead
    while cur:
        tem = cur.next
        cur.next = pre
        pre = cur
        cur = tem
    return pre
