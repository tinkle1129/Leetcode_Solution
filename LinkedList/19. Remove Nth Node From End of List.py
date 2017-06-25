###########################################
# Author: Tinkle
# E-mail: shutingnupt@gmail.com
# Name:  Remove Nth Node From End of List.py
# Creation Time: 2017/6/25
###########################################
'''
Given a linked list, remove the nth node from the end of list and return its head.

For example,

   Given linked list: 1->2->3->4->5, and n = 2.

   After removing the second node from the end, the linked list becomes 1->2->3->5.
Note:
Given n will always be valid.
Try to do this in one pass.
'''
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        ans = ListNode(0)
        ans.next = head

        p = ans
        q = ans

        for i in range(n):
            q = q.next

        while(q.next):
            p = p.next
            q = q.next

        dele = p.next
        p.next = dele.next
        del dele
        return ans.next


head = ListNode(1)
head.next = ListNode(2)
head.next.next= ListNode(3)
head.next.next.next= ListNode(4)
head.next.next.next.next= ListNode(5)

S = Solution()
q = S.removeNthFromEnd(head,2)
while(q):
    print q.val
    q = q.next