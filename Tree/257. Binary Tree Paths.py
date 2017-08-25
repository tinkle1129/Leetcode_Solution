# - * - coding:utf8 - * - -
###########################################
# Author: Tinkle
# E-mail: shutingnjupt@gmail.com
# Name:  Binary Tree Paths.py
# Creation Time: 2017/8/25
###########################################
'''
Given a binary tree, return all root-to-leaf paths.

For example, given the following binary tree:

   1
 /   \
2     3
 \
  5
All root-to-leaf paths are:

["1->2->5", "1->3"]
'''


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        ret = []
        if root == None:
            return ret
        cur_val = root.val
        if root.left:
            ret += self.binaryTreePaths(root.left)
        if root.right:
            ret += self.binaryTreePaths(root.right)
        if ret == []:
            return [str(cur_val)]
        else:
            for i in range(len(ret)):
                ret[i] = str(cur_val)+'->'+ret[i]
            return ret
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)

root.left.right = TreeNode(5)
S = Solution()
print S.binaryTreePaths(root)