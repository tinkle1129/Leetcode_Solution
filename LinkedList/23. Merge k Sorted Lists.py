# - * - coding:utf8 - * - -
###########################################
# Author: Tinkle
# E-mail: shutingnjupt@gmail.com
# Name:  Merge k Sorted Lists.py
# Creation Time: 2018/2/17
###########################################
'''
Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.
'''


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        ans = ListNode(0)
        tmp = ans
        while (l1 and l2):
            if l1.val < l2.val:
                tmp.next = ListNode(l1.val)
                tmp = tmp.next
                l1 = l1.next
            else:
                tmp.next = ListNode(l2.val)
                tmp = tmp.next
                l2 = l2.next
        while (l1):
            tmp.next = ListNode(l1.val)
            tmp = tmp.next
            l1 = l1.next
        while (l2):
            tmp.next = ListNode(l2.val)
            tmp = tmp.next
            l2 = l2.next
        return ans.next

    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        if len(lists) == 0:
            return None
        if len(lists) == 1:
            return lists[0]
        if len(lists) == 2:
            return self.mergeTwoLists(lists[0], lists[1])
        return self.mergeTwoLists(self.mergeKLists(lists[0:len(lists) / 2]), self.mergeKLists(lists[len(lists) / 2:]))