# - * - coding:utf8 - * - -
###########################################
# Author: Tinkle
# E-mail: shutingnjupt@gmail.com
# Name:  Palindrome Linked List.py
# Creation Time: 2018/2/17
###########################################
'''
Given a singly linked list, determine if it is a palindrome.
Follow up:
Could you do it in O(n) time and O(1) space?
'''
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
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head==None or head.next==None:
            return True
        fast=head
        slow=head
        while(fast and fast.next):
            slow=slow.next
            fast=fast.next.next
        if fast:
            slow=self.reverseList(slow.next)
        else:
            slow=self.reverseList(slow)
        while(slow):
            if head.val!=slow.val:
                return False
            slow=slow.next
            head=head.next
        return True