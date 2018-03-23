# - * - coding:utf8 - * - -
###########################################
# Author: Tinkle
# E-mail: shutingnjupt@gmail.com
# Name: Binary Tree Zigzag Level Order Traversal.py
# Creation Time: 2018/3/7
###########################################
'''
Given a binary tree, return the zigzag level order traversal of its nodes' values. (ie, from left to right, then right to left for the next level and alternate between).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its zigzag level order traversal as:
[
  [3],
  [20,9],
  [15,7]
]
'''


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        ret, stack, step = [], [], 0
        if root == None: return ret
        stack.append(root)
        while (stack):
            tmpstack = []
            tmp = []
            for node in stack:
                tmp.append(node.val)
                if node.left:
                    tmpstack.append(node.left)
                if node.right:
                    tmpstack.append(node.right)
            if step % 2:
                tmp = tmp[::-1]
            ret.append(tmp[:])
            step += 1
            stack = tmpstack[:]
        return ret

