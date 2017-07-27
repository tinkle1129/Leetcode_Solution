# - * - coding:utf8 - * - -
###########################################
# Author: Tinkle
# E-mail: shutingnjupt@gmail.com
# Name: Linked List Cycle II.py
# Creation Time: 2017/7/27
###########################################
'''
Given a linked list, return the node where the cycle begins. If there is no cycle, return null.

Note: Do not modify the linked list.
'''


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None or head.next == None:
            return None
        fast = slow = head
        while(fast and fast.next):
            slow = slow.next
            fast = fast.next.next
            if fast == slow:
                fast = head
                while(fast!=slow):
                    slow = slow.next
                    fast = fast.next
                return fast
        return None