# - * - coding:utf8 - * - -
###########################################
# Author: Tinkle
# E-mail: shutingnjupt@gmail.com
# Name:  Reverse Linked List.py
# Creation Time: 2018/2/17
###########################################
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head==None:
            return None
        p1=None
        p2=head
        while(p2):
            tmp=p2.next
            p2.next=p1
            p1=p2
            p2=tmp
        return p1