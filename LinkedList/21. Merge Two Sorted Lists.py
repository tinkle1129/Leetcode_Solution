###########################################
# Author: Tinkle
# E-mail: shutingnupt@gmail.com
# Name:  Merge Two Sorted Lists.py
# Creation Time: 2017/6/26
###########################################
'''
Merge two sorted linked lists and return it as a new list.
The new list should be made by splicing together the nodes of the first two lists.
'''
# Definition for singly-linked list.
class ListNode(object):
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        ans = ListNode(0)
        tmp = ans
        while(l1 and l2):
            if l1.val<l2.val:
                tmp.next = ListNode(l1.val)
                tmp = tmp.next
                l1 = l1.next
            else:
                tmp.next = ListNode(l2.val)
                tmp = tmp.next
                l2 = l2.next
        while(l1):
            tmp.next = ListNode(l1.val)
            tmp = tmp.next
            l1 = l1.next
        while(l2):
            tmp.next = ListNode(l2.val)
            tmp = tmp.next
            l2 = l2.next
        return ans.next

S = Solution()
l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(7)

l2 = ListNode(3)
l2.next = ListNode(4)
l2.next.next = ListNode(5)
l2.next.next.next = ListNode(8)

l3 = S.mergeTwoLists(l1,l2)
while(l3):
    print l3.val
    l3 = l3.next
