# - * - coding:utf8 - * - -
###########################################
# Author: Tinkle
# E-mail: shutingnupt@gmail.com
# Name: Remove Duplicates from Sorted List II.py
# Creation Time: 2017/7/12
###########################################
'''
Given a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list.

For example,
Given 1->2->3->3->4->4->5, return 1->2->5.
Given 1->1->1->2->3, return 2->3.
'''


# Definition for singly-linked list.
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
        cnt = 1

        while(pos_ptr):
            #print pos_ptr.val
            next_prt = pos_ptr.next

            if next_prt:
                if next_prt.val==pos_ptr.val:
                    cnt+=1
                else:
                    if cnt == 1:
                        current_ptr.next = ListNode(pos_ptr.val)
                        current_ptr = current_ptr.next
                    cnt = 1
            else:
                if cnt == 1:
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












