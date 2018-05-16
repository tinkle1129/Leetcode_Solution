###########################################
# Author: Tinkle
# E-mail: shutingnupt@gmail.com
# Name:  Unique Binary Search Trees II.py
# Creation Time: 2018/5/16
###########################################
'''

Given an integer n, generate all structurally unique BST's (binary search trees) that store values 1 ... n.

Example:

Input: 3
Output:
[
  [1,null,3,2],
  [3,2,null,1],
  [3,1,null,null,2],
  [2,1,3],
  [1,null,2,null,3]
]
Explanation:
The above output corresponds to the 5 unique BST's shown below:

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3
'''


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        arrays = [i for i in range(1, n + 1)]
        return self.dp(arrays)

    def dp(self, arrays):
        if len(arrays) == 1:
            return [TreeNode(arrays[0])]

        ret = []
        for k in range(len(arrays)):
            num = arrays[k]
            l = arrays[0:k]
            r = arrays[k + 1:]
            left = self.dp(l)
            right = self.dp(r)

            if left == []:
                for j in range(len(right)):
                    Node = TreeNode(num)
                    Node.right = right[j]
                    ret.append(Node)

            if right == []:
                for i in range(len(left)):
                    Node = TreeNode(num)
                    Node.left = left[i]
                    ret.append(Node)

            for i in range(len(left)):
                for j in range(len(right)):
                    Node = TreeNode(num)
                    Node.left = left[i]
                    Node.right = right[j]
                    ret.append(Node)

        return ret

S = Solution()
print S.generateTrees(3)
