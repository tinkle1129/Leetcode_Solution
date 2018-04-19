# - * - coding:utf8 - * - -
###########################################
# Author: Tinkle
# E-mail: shutingnjupt@gmail.com
# Name: Find Bottom Left Tree Value.py
# Creation Time: 2018/4/8
###########################################
'''
Given a binary tree, find the leftmost value in the last row of the tree.

Example 1:
Input:

    2
   / \
  1   3

Output:
1
Example 2:
Input:

        1
       / \
      2   3
     /   / \
    4   5   6
       /
      7

Output:
7
Note: You may assume the tree (i.e., the given root node) is not NULL.
'''
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findBottomLeftValueDFS(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None: return 0
        def dfs(root,step):
            maxstep = step
            val = root.val
            if root.left:
                leftstep,lval = dfs(root.left,step+1)
                if leftstep>maxstep:
                    maxstep = leftstep
                    val = lval
            if root.right:
                rightstep,rval = dfs(root.right,step+1)
                if rightstep>maxstep:
                    maxstep = rightstep
                    val = rval
            return maxstep,val
        maxstep,val = dfs(root,0)
        return val
    def findBottomLeftValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None: return 0
        queue = [root]
        while(queue):
            tmp = []
            for q in queue:
                if q.left:
                    tmp.append(q.left)
                if q.right:
                    tmp.append(q.right)
            if tmp == []:
                return queue[0].val
            queue = tmp[:]