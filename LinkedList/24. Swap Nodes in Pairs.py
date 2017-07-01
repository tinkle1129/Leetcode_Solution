###########################################
# Author: Tinkle
# E-mail: shutingnupt@gmail.com
# Name:  Swap Nodes in Pairs.py
# Creation Time: 2017/6/30
###########################################
'''
Given a linked list, swap every two adjacent nodes and return its head.

For example,
Given 1->2->3->4, you should return the list as 2->1->4->3.

Your algorithm should use only constant space. You may not modify the values in the list, only nodes itself can be changed.
'''
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        ans = ListNode(0)
        ans.next = head
        tmp = ans
        while (tmp!=None and tmp.next!=None and tmp.next.next!=None):
            p1 = tmp.next
            p2 = tmp.next.next
            tmp1 = p2.next
            p2.next = p1
            p1.next = tmp1
            tmp.next = p2
            tmp = tmp.next.next
        return ans.next

head = ListNode(1)
#head.next = ListNode(2)
#head.next.next = ListNode(3)
#head.next.next.next = ListNode(4)

S = Solution()
a = S.swapPairs(head)
while(a!=None):
    print a.val
    a = a.next

