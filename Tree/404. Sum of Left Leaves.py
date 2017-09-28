# - * - coding:utf8 - * - -
###########################################
# Author: Tinkle
# E-mail: shutingnjupt@gmail.com
# Name: Sum of Left Leaves.py
# Creation Time: 2017/9/28
###########################################
'''
Find the sum of all left leaves in a given binary tree.

Example:

    3
   / \
  9  20
    /  \
   15   7

There are two left leaves in the binary tree, with values 9 and 15 respectively. Return 24.
'''


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        def sumofleftLeaves(root, state):
            if root == None:
                return 0
            if root.left == None and root.right == None and state == 1:
                return root.val
            return sumofleftLeaves(root.left, 1) + sumofleftLeaves(root.right, 0)

        return sumofleftLeaves(root, 0)
