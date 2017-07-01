###########################################
# Author: Tinkle
# E-mail: shutingnupt@gmail.com
# Name:  Reverse Nodes in k-Group.py
# Creation Time: 2017/6/30
###########################################
'''
Given a linked list, reverse the nodes of a linked list k at a time and return its modified list.

k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes in the end should remain as it is.

You may not alter the values in the nodes, only nodes itself may be changed.

Only constant memory is allowed.

For example,
Given this linked list: 1->2->3->4->5

For k = 2, you should return: 2->1->4->3->5

For k = 3, you should return: 3->2->1->4->5
'''
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseKGroup(self, head, k):
        # Need help
        if head == None: return head
        dummy = ListNode(0)
        dummy.next = head
        start = dummy  # start =0.   Given this linked list: 1->2->3->4->5    #    For k = 2, you should return: 2->1->4->3->5
        while start.next:
            end = start  # end = 0
            for i in range(k - 1):
                end = end.next  # end = 1
                if end.next == None: return dummy.next
            (start.next, start) = self.reverse(start.next,
                                               end.next)  # (start.next=3, start=1)=self.reverse(start.next=1, end.next=2)
        return dummy.next

    def reverse(self, start, end):
        dummy = ListNode(0)
        dummy.next = start
        while dummy.next != end:
            tmp = start.next
            start.next = tmp.next
            tmp.next = dummy.next
            dummy.next = tmp
        return (end, start)

head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)
S= Solution()
ans = S.reverseKGroup(head,2)
while(ans):
    print ans.val
    ans = ans.next
