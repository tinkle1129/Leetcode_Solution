# - * - coding:utf8 - * - -
###########################################
# Author: Tinkle
# E-mail: shutingnupt@gmail.com
# Name: Remove Duplicates from Sorted List .py
# Creation Time: 2017/7/12
###########################################
'''
Given a sorted linked list, delete all duplicates such that each element appear only once.

For example,
Given 1->1->2, return 1->2.
Given 1->1->2->3->3, return 1->2->3.
'''
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        ret = ListNode(0)
        pos_ptr = head
        current_ptr = ret

        while(pos_ptr):
            next_prt = pos_ptr.next

            if next_prt:
                if next_prt.val!=pos_ptr.val:
                    current_ptr.next = ListNode(pos_ptr.val)
                    current_ptr = current_ptr.next
            else:
                current_ptr.next = ListNode(pos_ptr.val)
                current_ptr = current_ptr.next

            pos_ptr = pos_ptr.next

        return ret.next

head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(3)
head.next.next.next.next = ListNode(4)
head.next.next.next.next.next = ListNode(4)
head.next.next.next.next.next.next = ListNode(5)

S = Solution()
ret =  S.deleteDuplicates(head)
while(ret):
    print ret.val
    ret = ret.next

head1 = ListNode(1)
head1.next = ListNode(1)
head1.next.next = ListNode(1)
head1.next.next.next = ListNode(2)
head1.next.next.next.next = ListNode(3)

ret1 =  S.deleteDuplicates(head1)
while(ret1):
    print ret1.val
    ret1 = ret1.next






