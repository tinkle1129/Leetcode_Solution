# - * - coding:utf8 - * - -
###########################################
# Author: Tinkle
# E-mail: shutingnjupt@gmail.com
# Name: Linked List Random Node.py
# Creation Time: 2017/9/24
###########################################
'''
Given a singly linked list, return a random node's value from the linked list. Each node must have the same probability of being chosen.

Follow up:
What if the linked list is extremely large and its length is unknown to you? Could you solve this efficiently without using extra space?

Example:

// Init a singly linked list [1,2,3].
ListNode head = new ListNode(1);
head.next = new ListNode(2);
head.next.next = new ListNode(3);
Solution solution = new Solution(head);

// getRandom() should return either 1, 2, or 3 randomly. Each element should have equal probability of returning.
solution.getRandom();

'''
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
import random


class Solution(object):
    def __init__(self, head):
        """
        @param head The linked list's head.
        Note that the head is guaranteed to be not null, so it contains at least one node.
        :type head: ListNode
        """
        self.head = head
        self.length = 0
        ans = head
        while (ans):
            self.length += 1
            ans = ans.next

    def getRandom(self):
        """
        Returns a random node's value.
        :rtype: int
        """
        index = random.randint(1, self.length) - 1
        idx = 0
        ans = self.head
        while (idx < index):
            ans = ans.next
            idx += 1
        return ans.val



        # Your Solution object will be instantiated and called as such:
        # obj = Solution(head)
        # param_1 = obj.getRandom()