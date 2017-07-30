# - * - coding:utf8 - * - -
###########################################
# Author: Tinkle
# E-mail: shutingnjupt@gmail.com
# Name: Convert Sorted List to Binary Search Tree.py
# Creation Time: 2017/7/29
###########################################
'''
Given a singly linked list where elements are sorted in ascending order,
convert it to a height balanced BST.
'''


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        if head == None:
            return None
        if head.next == None:
            return TreeNode(head.val)
        fast = slow = head
        while(fast.next and fast.next.next):
            slow = slow.next
            fast = fast.next.next
        root = TreeNode(slow.val)
        right = slow.next
        left = ListNode(0)
        left.next = head
        tmp = left
        while(tmp.next!=slow):
            tmp = tmp.next
        tmp.next = None
        left = left.next
        root.left = self.sortedListToBST(left)
        root.right = self.sortedListToBST(right)
        return root
