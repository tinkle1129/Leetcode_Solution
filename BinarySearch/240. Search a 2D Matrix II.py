# - * - coding:utf8 - * - -
###########################################
# Author: Tinkle
# E-mail: shutingnjupt@gmail.com
# Name:  Search a 2D Matrix II.py
# Creation Time: 2017/8/25
###########################################
'''
Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

Integers in each row are sorted in ascending from left to right.
Integers in each column are sorted in ascending from top to bottom.
For example,

Consider the following matrix:

[
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]
Given target = 5, return true.

Given target = 20, return false.
'''


class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if len(matrix)==0 or len(matrix[0])==0:
            return False
        i = 0
        j = len(matrix[0])-1
        while(i<len(matrix) and j>=0):
            if target == matrix[i][j]:
                return True
            elif target<matrix[i][j]:
                j-=1
            else:
                i+=1
        return False
S = Solution()
'''
matrix = [
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]
#print S.searchMatrix(matrix,5)
print S.searchMatrix(matrix,20)
'''
print S.searchMatrix([[1,2,3,4,5],
                      [6,7,8,9,10],
                      [11,12,13,14,15],
                      [16,17,18,19,20],
                      [21,22,23,24,25]],5)
