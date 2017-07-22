# - * - coding:utf8 - * - -
###########################################
# Author: Tinkle
# E-mail: shutingnjupt@gmail.com
# Name: Partition List.py
# Creation Time: 2017/7/21
###########################################
'''
Given a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.

You should preserve the original relative order of the nodes in each of the two partitions.

For example,
Given 1->4->3->2->5->2 and x = 3,
return 1->2->2->4->3->5.
'''
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        lessNode = ListNode(0)
        moreNode = ListNode(0)
        less_ptr = lessNode
        more_ptr = moreNode
        while(head):
            if head.val < x :
                less_ptr.next = ListNode(head.val)
                less_ptr = less_ptr.next
            else:
                more_ptr.next = ListNode(head.val)
                more_ptr = more_ptr.next
            head = head.next
        less_ptr.next = moreNode.next
        return lessNode.next

head = ListNode(1)
head.next = ListNode(4)
head.next.next = ListNode(3)
head.next.next.next = ListNode(2)
head.next.next.next.next = ListNode(5)
head.next.next.next.next.next = ListNode(2)

S = Solution()
ans = S.partition(head,3)

while(ans):
    print ans.val
    ans = ans.next