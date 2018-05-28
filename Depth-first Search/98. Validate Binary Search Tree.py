###########################################
# Author: Tinkle
# E-mail: shutingnjupt@gmail.com
# Name:  Validate Binary Search Tree.py
# Creation Time: 2018/5/17
###########################################
'''
Given a binary tree, determine if it is a valid binary search tree (BST).

Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.
Example 1:

Input:
    2
   / \
  1   3
Output: true
Example 2:

    5
   / \
  1   4
     / \
    3   6
Output: false
Explanation: The input is: [5,1,4,null,null,3,6]. The root node's value
             is 5 but its right child's value is 4.
'''


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return True
        if root.left is None and root.right is None:
            return True
        if root.left is None:
            return root.val < self.minvalue(root.right) and self.isValidBST(root.right)
        elif root.right is None:
            return root.val > self.maxvalue(root.left) and self.isValidBST(root.left)
        else:
            return root.val < self.minvalue(root.right) and self.isValidBST(root.right) and root.val > self.maxvalue(
                root.left) and self.isValidBST(root.left)

    def maxvalue(self, root):
        if root.left is None and root.right is None:
            return root.val
        if root.left is None:
            return max(root.val, self.maxvalue(root.right))
        if root.right is None:
            return max(root.val, self.maxvalue(root.left))
        return max(root.val, self.maxvalue(root.left), self.maxvalue(root.right))

    def minvalue(self, root):
        if root.left is None and root.right is None:
            return root.val
        if root.left is None:
            return min(root.val, self.maxvalue(root.right))
        if root.right is None:
            return min(root.val, self.maxvalue(root.left))
        return min(root.val, self.maxvalue(root.left), self.maxvalue(root.right))


import sys


class Solutions(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        min_ = -sys.maxint
        max_ = sys.maxint
        return self.checkBST(root, min_, max_)

    def checkBST(self, root, min_, max_):
        if root is None: return True
        if root.val <= min_ or root.val >= max_:
            return False
        return self.checkBST(root.left, min_, root.val) and self.checkBST(root.right, root.val, max_)
    