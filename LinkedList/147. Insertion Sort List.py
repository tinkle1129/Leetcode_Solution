# - * - coding:utf8 - * - -
###########################################
# Author: Tinkle
# E-mail: shutingnjupt@gmail.com
# Name: Insertion Sort List.py
# Creation Time: 2017/7/28
###########################################
'''
Sort a linked list using insertion sort.
'''


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        ans = ListNode(0)
        head_ptr = head
        while(head_ptr):
            ptr = ans.next
            last = ans
            while(ptr and ptr.val<head_ptr.val):
                last = ptr
                ptr = ptr.next
            if ptr:
                last.next = ListNode(head_ptr.val)
                last.next.next = ptr
            else:
                last.next = ListNode(head_ptr.val)
            head_ptr = head_ptr.next

        return ans.next
