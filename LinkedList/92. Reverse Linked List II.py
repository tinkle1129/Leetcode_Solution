# - * - coding:utf8 - * - -
###########################################
# Author: Tinkle
# E-mail: shutingnjupt@gmail.com
# Name: Reverse Linked List II.py
# Creation Time: 2017/7/21
###########################################
'''
Reverse a linked list from position m to n. Do it in-place and in one-pass.

For example:
Given 1->2->3->4->5->NULL, m = 2 and n = 4,

return 1->4->3->2->5->NULL.

Note:
Given m, n satisfy the following condition:
1 ? m ? n ? length of list.
'''


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):

    def reverseBetween(self, head, m, n):

        if head is None or head.next is None:

            return head
        ans = ListNode(0)
        ans.next = head
        ptr = ans
        for i in range(m-1):
            ptr = ptr.next
        cur_ptr = ptr.next
        for i in range(n-m):
            tmp = cur_ptr.next
            cur_ptr.next = tmp.next
            tmp.next = ptr.next
            ptr.next = tmp
        return ans.next

head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)

S = Solution()
out = S.reverseBetween(head,2,4)
while(out):
    print out.val
    out = out.next

