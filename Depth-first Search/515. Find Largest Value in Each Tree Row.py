# - * - coding:utf8 - * - -
###########################################
# Author: Tinkle
# E-mail: shutingnjupt@gmail.com
# Name: Find Largest Value in Each Tree Row.py
# Creation Time: 2018/4/8
###########################################
'''
You need to find the largest value in each row of a binary tree.

Example:
Input:

          1
         / \
        3   2
       / \   \
      5   3   9

Output: [1, 3, 9]
'''


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def largestValues(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        steps = dict()

        def dfs(root, step):
            if root is None:
                return
            if step not in steps:
                steps[step] = root.val
            else:
                steps[step] = max(steps[step], root.val)
            if root.left:
                dfs(root.left, step + 1)
            if root.right:
                dfs(root.right, step + 1)

        dfs(root, 0)
        ans = sorted(steps.items(), key=lambda x: x[0])
        ret = list(map(lambda x: x[1], ans))

        return ret

    def largestValuesBFS(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root is None: return []
        queue = [root]
        ret = []
        while (queue):
            tmp = []
            val = None
            for q in queue:
                if q.left:
                    tmp.append(q.left)
                if q.right:
                    tmp.append(q.right)
                if val is None:
                    val = q.val
                else:
                    val = max(val, q.val)
            queue = tmp[:]
            ret.append(val)
        return ret
