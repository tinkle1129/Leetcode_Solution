# - * - coding:utf8 - * - -
###########################################
# Author: Tinkle
# E-mail: shutingnjupt@gmail.com
# Name:  House Robber III.py
# Creation Time: 2017/9/5
###########################################
'''
The thief has found himself a new place for his thievery again. There is only one entrance to this area, called the "root." Besides the root, each house has one and only one parent house. After a tour, the smart thief realized that "all houses in this place forms a binary tree". It will automatically contact the police if two directly-linked houses were broken into on the same night.

Determine the maximum amount of money the thief can rob tonight without alerting the police.

Example 1:
     3
    / \
   2   3
    \   \
     3   1
Maximum amount of money the thief can rob = 3 + 3 + 1 = 7.
Example 2:
     3
    / \
   4   5
  / \   \
 1   3   1
Maximum amount of money the thief can rob = 4 + 5 = 9.
'''


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        dic = {}
        dic_1 = {}
        def dfs(root,state):
            if root == None:
                return 0
            if root.left not in dic_1:
                dic_1[root.left] = dfs(root.left,0)
            if root.right not in dic_1:
                dic_1[root.right] = dfs(root.right,0)
            ans2 = dic_1[root.left]+dic_1[root.right]
            if state == 0: # can select or not:
                if root.left not in dic:
                    dic[root.left] = dfs(root.left,1)
                if root.right not in dic:
                    dic[root.right] = dfs(root.right,1)
                ans1 = root.val + dic[root.left] + dic[root.right]
                return max(ans1,ans2)
            else: # selected
                return ans2
        return dfs(root,0)