# - * - coding:utf8 - * - -
###########################################
# Author: Tinkle
# E-mail: shutingnjupt@gmail.com
# Name: Reorder List.py
# Creation Time: 2017/7/27
###########################################
'''
Given a singly linked list L: L0?L1?…?Ln-1?Ln,
reorder it to: L0?Ln?L1?Ln-1?L2?Ln-2?…

You must do this in-place without altering the nodes' values.

For example,
Given {1,2,3,4}, reorder it to {1,4,2,3}.
'''
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """
        if head == None or head.next == None:
            return
        fast = slow = head
        while(fast and fast.next):
            slow = slow.next
            fast = fast.next.next
        left = head
        right = slow.next
        slow.next = None

        # Reverse
        dummy = ListNode(0);dummy.next = right
        p = right.next; right.next = None
        while(p):
            tmp = p;  p = p.next
            tmp.next = dummy.next
            dummy.next = tmp
        right = dummy.next

        l = left;r = right
        while r:
            tmp1 = l.next;tmp2 = r.next
            l.next = r;r.next=tmp1
            l = tmp1;r = tmp2

head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next =ListNode(4)
#head.next.next.next.next = ListNode(5)

S = Solution()
S.reorderList(head)

while(head):
    print head.val
    head = head.next
