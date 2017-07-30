# - * - coding:utf8 - * - -
###########################################
# Author: Tinkle
# E-mail: shutingnjupt@gmail.com
# Name: Binary Tree Level Order Traversal II.py
# Creation Time: 2017/7/29
###########################################
'''
Given a binary tree, return the bottom-up level order traversal of its nodes' values. (ie, from left to right, level by level from leaf to root).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its bottom-up level order traversal as:
[
  [15,7],
  [9,20],
  [3]
]

'''


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        dict_ = {}
        if root == None:
            return  []
        queue = [(root,0)]
        while(len(queue)):
            query = queue.pop(0)
            dict_.setdefault(query[1],[])
            dict_[query[1]].append(query[0].val)
            if query[0].left:
                queue.append((query[0].left,query[1]+1))
            if query[0].right:
                queue.append((query[0].right,query[1]+1))
        return list(map(lambda x:x[1],sorted(dict_.items(),key=lambda x:x[0],reverse=True)))
