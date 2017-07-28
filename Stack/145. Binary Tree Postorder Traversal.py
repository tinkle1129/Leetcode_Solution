# - * - coding:utf8 - * - -
###########################################
# Author: Tinkle
# E-mail: shutingnjupt@gmail.com
# Name: Binary Tree Postorder Traversal.py
# Creation Time: 2017/7/28
###########################################
'''
Given a binary tree, return the postorder traversal of its nodes' values.

For example:
Given binary tree {1,#,2,3},
   1
    \
     2
    /
   3
return [3,2,1].

Note: Recursive solution is trivial, could you do it iteratively?
'''


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        ret = []
        if root == None:
            return ret
        stack  = [root]
        while(len(stack)):
            query = stack.pop()
            if query.left == None and query.right == None:
                ret.append(query.val)
            else:
                stack.append(TreeNode(query.val))
                if query.right:
                    stack.append(query.right)
                if query.left:
                    stack.append(query.left)
        return ret
