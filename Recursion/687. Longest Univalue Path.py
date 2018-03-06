# - * - coding:utf8 - * - -
###########################################
# Author: Tinkle
# E-mail: shutingnjupt@gmail.com
# Name: Partition to K Equal Sum Subsets.py
# Creation Time: 2018/3/6
###########################################
'''
Given a binary tree, find the length of the longest path where each node in the path has the same value. This path may or may not pass through the root.

Note: The length of path between two nodes is represented by the number of edges between them.

Example 1:

Input:

              5
             / \
            4   5
           / \   \
          1   1   5
Output:

2
Example 2:

Input:

              1
             / \
            4   5
           / \   \
          4   4   5
Output:

2
Note: The given binary tree has not more than 10000 nodes. The height of the tree is not more than 1000.


'''


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def longestUnivaluePath(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root: return 0
        left, right, val = root.left, root.right, root.val
        return max(self.longestlength(left, val) + self.longestlength(right, val),
                   self.longestUnivaluePath(left), self.longestUnivaluePath(right))

    def longestlength(self, root, val):
        if not root or root.val != val:  return 0
        return 1 + max(self.longestlength(root.left, val), self.longestlength(root.right, val))
