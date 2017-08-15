# - * - coding:utf8 - * - -
###########################################
# Author: Tinkle
# E-mail: shutingnjupt@gmail.com
# Name: Binary Tree Right Side View
# Creation Time: 2017/8/13
###########################################
'''
Given a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

For example:
Given the following binary tree,
   1            <---
 /   \
2     3         <---
 \     \
  5     4       <---
You should return [1, 3, 4].
'''


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root == None:
            return []
        queue = []
        queue.append((root,0))
        ret = []
        while(len(queue)):
            cur = queue.pop()
            cur_node = cur[0]
            index = cur[1]
            if index>=len(ret):
                ret.append(cur_node.val)
            if cur_node.left:
                queue.append((cur_node.left,index+1))
            if cur_node.right:
                queue.append((cur_node.right,index+1))
        return ret

root = TreeNode(1)
root.left = TreeNode(2)
root.left.left = TreeNode(4)
root.right = TreeNode(3)

S = Solution()
print S.rightSideView(root)


