# - * - coding:utf8 - * - -
###########################################
# Author: Tinkle
# E-mail: shutingnupt@gmail.com
# Name:  Rotate List.py
# Creation Time: 2017/7/7
###########################################
'''
Given a list, rotate the list to the right by k places, where k is non-negative.

For example:
Given 1->2->3->4->5->NULL and k = 2,
return 4->5->1->2->3->NULL.
'''


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        cnt = 0
        tmp = head
        while(tmp):
            cnt +=1
            tmp = tmp.next

        k = k % cnt
        if k == 0 or head==None:
            return head

        header = head
        pointer = head
        pos = 0
        while(pointer and pos<(cnt-k-1)):
            pos +=1
            pointer = pointer.next

        new_header = pointer.next
        pointer.next = None
        pointer = new_header
        while(pointer.next):
            pointer = pointer.next
        pointer.next = header
        return new_header

head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)

tmp = head
while(tmp):
    print tmp.val
    tmp = tmp.next

S = Solution()
ans = S.rotateRight(head,10)
while(ans):
    print ans.val
    ans = ans.next

