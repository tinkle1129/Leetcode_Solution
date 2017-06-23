###########################################
# Author: Tinkle
# E-mail: shutingnupt@gmail.com
# Name: Add Two Numbers.py
# Creation Time: 2017/6/20
###########################################
'''
Describe:
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.
You may assume the two numbers do not contain any leading zero, except the number 0 itself.
Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
'''
class ListNode(object):
    def __init__(self,x):
        self.val = x
        self.next = None

class Solution(object):
    def addTwoNumbers(self,l1,l2):
        '''
        :param l1: ListNode
        :param l2: ListNode
        :return: ListNode
        '''
        flag = 0
        p = None
        while(l1!=None or l2!=None):
            ans = flag
            if l1!=None:
                ans +=l1.val
                l1 = l1.next
            if l2!=None:
                ans +=l2.val
                l2 = l2.next
            flag = ans/10
            ans = ans %10
            if p == None:
                ret = p = ListNode(ans)
            else:
                p.next = ListNode(ans)
                p = p.next

        if flag>0:
            p.next = ListNode(flag)
        return ret
'''
# Test Func
L1 = ListNode(2)
L1.next = ListNode(4)
L1.next.next = ListNode(9)
L1.next.next.next = ListNode(9)

L2 = ListNode(5)
L2.next= ListNode(6)
L2.next.next = ListNode(4)

S = Solution()
ans = S.addTwoNumbers(L1,L2)
while(ans!=None):
    print ans.val
    ans = ans.next
'''