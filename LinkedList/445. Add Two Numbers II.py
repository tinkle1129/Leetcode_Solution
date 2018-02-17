# - * - coding:utf8 - * - -
###########################################
# Author: Tinkle
# E-mail: shutingnjupt@gmail.com
# Name:  Add Two Numbers II.py
# Creation Time: 2018/2/17
###########################################
'''
You are given two non-empty linked lists representing two non-negative integers. The most significant digit comes first and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Follow up:
What if you cannot modify the input lists? In other words, reversing the lists is not allowed.

Example:

Input: (7 -> 2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 8 -> 0 -> 7
'''


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        size1 = self.getSize(l1)
        size2 = self.getSize(l2)
        length = max(size1,size2)
        print size1,size2,length

        p = h = ListNode(0)
        while(length):
            p.next = ListNode(0)
            p = p.next
            if length<=size1:
                p.val += l1.val
                l1 = l1.next
            if length<=size2:
                p.val += l2.val
                l2 = l2.next
            length-=1

        p = h
        while(p):
            q = p.next
            while q and q.val==9:
                q = q.next
            if q and q.val > 9:
                while p!=q:
                    p.val +=1
                    p = p.next
                    p.val -=10
            else:
                p = q
        return h if h.val else h.next


    def getSize(self,root):
        pos = root
        size = 0
        while(pos):
            size+=1
            pos = pos.next
        return size

Node = ListNode(7)
Node.next = ListNode(2)
Node.next.next = ListNode(4)
Node.next.next.next = ListNode(3)

Node2 = ListNode(5)
Node2.next = ListNode(6)
Node2.next.next = ListNode(4)

S = Solution()
print S.addTwoNumbers(Node,Node2)
