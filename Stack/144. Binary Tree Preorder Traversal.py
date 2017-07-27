# - * - coding:utf8 - * - -
###########################################
# Author: Tinkle
# E-mail: shutingnjupt@gmail.com
# Name: Binary Tree Preorder Traversal.py
# Creation Time: 2017/7/27
###########################################
'''
Given a binary tree, return the preorder traversal of its nodes' values.

For example:
Given binary tree {1,#,2,3},
   1
    \
     2
    /
   3
return [1,2,3].

Note: Recursive solution is trivial, could you do it iteratively?
'''


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root == None:
            return []
        ret = []
        stack = [root]
        while(len(stack)):
            query = stack.pop(0)
            ret.append(query.val)
            if query.right:
                stack.insert(0,query.right)
            if query.left:
                stack.insert(0,query.left)
        return ret