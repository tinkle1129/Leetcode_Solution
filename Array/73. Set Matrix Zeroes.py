# - * - coding:utf8 - * - -
###########################################
# Author: Tinkle
# E-mail: shutingnupt@gmail.com
# Name:Set Matrix Zeroes.py
# Creation Time: 2017/7/10
###########################################
'''
Given a m x n matrix, if an element is 0, set its entire row and column to 0. Do it in place.

'''
class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        if m==0:
            return
        n = len(matrix[0])
        mark=1
        for i in range(m):
            if matrix[i][0] == 0:
                mark = 0
            for j in range(1,n):
                if matrix[i][j]==0:
                    matrix[i][0]=0
                    matrix[0][j]=0
        #print matrix,mark
        for i in range(m):
            for j in range(0,n-1):
                if matrix[m-1-i][0]==0 or matrix[0][n-1-j]==0:
                    matrix[m-1-i][n-1-j]=0
            if mark == 0:
                matrix[m - 1 - i][0] = 0