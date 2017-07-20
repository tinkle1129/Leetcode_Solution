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
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        ret = []
        def dfs(root,sum,tmp):
            if root != None:
                if root.left == None and root.right == None: # leaf node
                    if root.val == sum:
                        tmp.append(root.val)
                        ret.append(tmp[:])
                else:
                    tmp.append(root.val)
                    dfs(root.left,sum-root.val,tmp[:])
                    dfs(root.right,sum-root.val,tmp[:])
        dfs(root,sum,[])
        return ret


