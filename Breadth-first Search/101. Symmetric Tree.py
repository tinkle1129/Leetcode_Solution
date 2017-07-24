# - * - coding:utf8 - * - -
###########################################
# Author: Tinkle
# E-mail: shutingnjupt@gmail.com
# Name: Symmetric Tree.py
# Creation Time: 2017/7/23
###########################################
'''
Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

For example, this binary tree [1,2,2,3,4,4,3] is symmetric:

    1
   / \
  2   2
 / \ / \
3  4 4  3
But the following [1,2,2,null,3,null,3] is not:
    1
   / \
  2   2
   \   \
   3    3
Note:
Bonus points if you could solve it both recursively and iteratively.


'''


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root==None:
            return True
        return self.symetric(root.left,root.right)
    def symetric(self,root_a,root_b):
        if root_a==None and root_b==None:
            return True
        if root_a==None or root_b==None:
            return False
        if root_a.val !=root_b.val:
            return False
        return self.symetric(root_a.left,root_b.right) and self.symetric(root_a.right,root_b.left)
