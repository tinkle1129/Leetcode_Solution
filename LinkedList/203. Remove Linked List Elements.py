# - * - coding:utf8 - * - -
###########################################
# Author: Tinkle
# E-mail: shutingnjupt@gmail.com
# Name:  Remove Linked List Elements.py
# Creation Time: 2017/8/14
###########################################
'''
Remove all elements from a linked list of integers that have value val.

Example
Given: 1 --> 2 --> 6 --> 3 --> 4 --> 5 --> 6, val = 6
Return: 1 --> 2 --> 3 --> 4 --> 5

'''


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        ans = ListNode(0)
        ptr = ans
        cur_ptr = head
        while(cur_ptr):
            if cur_ptr.val!=val:
                ptr.next = ListNode(cur_ptr.val)
                ptr=ptr.next
            cur_ptr=cur_ptr.next
        return ans.next