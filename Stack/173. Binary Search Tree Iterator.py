# - * - coding:utf8 - * - -
###########################################
# Author: Tinkle
# E-mail: shutingnjupt@gmail.com
# Name: Binary Search Tree Iterator.py
# Creation Time: 2018/3/8
###########################################
'''
Implement an iterator over a binary search tree (BST). Your iterator will be initialized with the root node of a BST.

Calling next() will return the next smallest number in the BST.

Note: next() and hasNext() should run in average O(1) time and uses O(h) memory, where h is the height of the tree.

Credits:
Special thanks to @ts for adding this problem and creating all test cases.

Seen this question in a real interview before?
'''


# Definition for a  binary tree node
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class BSTIterator(object):
    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.stack = []
        self.preInsert(root)

    def hasNext(self):
        """
        :rtype: bool
        """
        return len(self.stack)

    def next(self):
        """
        :rtype: int
        """
        top = self.stack.pop()
        self.preInsert(top.right)
        return top.val

    def preInsert(self, root):
        while (root):
            self.stack.append(root)
            root = root.left
            # Your BSTIterator will be called like this:
            # i, v = BSTIterator(root), []
            # while i.hasNext(): v.append(i.next())