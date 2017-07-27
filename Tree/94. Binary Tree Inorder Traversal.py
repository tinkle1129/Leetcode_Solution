# - * - coding:utf8 - * - -
###########################################
# Author: Tinkle
# E-mail: shutingnjupt@gmail.com
# Name: Binary Tree Inorder Traversal.py
# Creation Time: 2017/7/25
###########################################
'''
Given a binary tree, return the inorder traversal of its nodes' values.

For example:
Given binary tree [1,null,2,3],
   1
    \
     2
    /
   3
return [1,3,2].

Note: Recursive solution is trivial, could you do it iteratively?
'''


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def inorderTraversal(self,root): # iterative
        '''
        :param root: TreeNode
        :return: List[int]
        '''
        stack = []
        ret = []
        if root == None:
            return []
        if root.right:
            stack.append(root.right)
        stack.append(TreeNode(root.val))
        if root.left:
            stack.append(root.left)
        while(stack):
            query = stack.pop()
            if query.left == None and query.right == None:
                ret.append(query.val)
            else:
                if query.right:
                    stack.append(query.right)
                stack.append(TreeNode(query.val))
                if query.left:
                    stack.append(query.left)
        return ret
    def inorderTraversal_(self, root): # Recursive
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        ret = []
        # left # root.val # right
        def find(root):
            if root:
                if root.left:
                    find(root.left)
                ret.append(root.val)
                if root.right:
                    find(root.right)
        find(root)
        return ret
head = TreeNode(1)
head.right = TreeNode(2)
head.right.left = TreeNode(3)
S = Solution()
print S.inorderTraversal(head)
