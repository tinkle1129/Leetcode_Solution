# - * - coding:utf8 - * - -
###########################################
# Author: Tinkle
# E-mail: shutingnjupt@gmail.com
# Name: Path Sum II.py
# Creation Time: 2017/7/20
###########################################
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        if root == None:
            return

        self.flatten(root.right)
        self.flatten(root.left)
        tmp = root
        if tmp.left == None:
            return
        tmp = tmp.left
        while(tmp.right!=None):
            tmp = tmp.right
        tmp.right = root.right
        root.right = root.left
        root.left = None
