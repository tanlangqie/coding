# -*- coding: utf-8 -*-#

# Name:   删除链表的第n个节点.py
# Author: tangzhuang
# Date:   2021/7/12
# desc:https://leetcode-cn.com/problems/remove-nth-node-from-end-of-list/

"""

给你一个链表，删除链表的倒数第 n 个结点，并且返回链表的头结点。
进阶：你能尝试使用一趟扫描实现吗？
"""

#思路：链表+1次遍历   栈或队列

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        List = []
        count = 0
        f = head
        while (head):
            List.append(head)
            head = head.next
            count = count + 1

        if n == count:
            return f.next
        List[-n - 1].next = List[-n].next
        return f
