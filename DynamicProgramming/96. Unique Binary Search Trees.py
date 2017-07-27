# - * - coding:utf8 - * - -
###########################################
# Author: Tinkle
# E-mail: shutingnjupt@gmail.com
# Name: Unique Binary Search Trees.py
# Creation Time: 2017/7/25
###########################################
'''
Given n, how many structurally unique BST's (binary search trees) that store values 1...n?

For example,
Given n = 3, there are a total of 5 unique BST's.

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3

'''


class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        ret = [1 for i in range(n+1)]
        for i in range(2,n+1):
            tmp = 0
            for j in range(i):
                tmp += ret[j]*ret[i-1-j]
            ret[i] = tmp
        return ret[n]

S = Solution()
print S.numTrees(4)
