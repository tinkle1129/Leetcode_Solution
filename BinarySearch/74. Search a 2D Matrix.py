# - * - coding:utf8 - * - -
###########################################
# Author: Tinkle
# E-mail: shutingnupt@gmail.com
# Name: Search a 2D Matrix.py
# Creation Time: 2017/7/10
###########################################
'''
Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

Integers in each row are sorted from left to right.
The first integer of each row is greater than the last integer of the previous row.
For example,

Consider the following matrix:

[
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
Given target = 3, return true.
'''
class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        l = len(matrix)
        if l == 0:
            return False
        if len(matrix[0])==0:
            return False
        start=0
        end=l-1
        while(start<=end):
            mid=(start+end)/2
            if matrix[mid][0] == target:
                return True
            elif matrix[mid][0] > target:
                end=mid-1
            else:
                start=mid+1
        if end<0:
            return False
        row=end
        #print mid
        start=0
        end=len(matrix[row])-1
        while(start<=end):
            mid=(start+end)/2
            if matrix[row][mid] ==target:
                return True
            elif matrix[row][mid] > target:
                end=mid-1
            else:
                start=mid+1
        return False