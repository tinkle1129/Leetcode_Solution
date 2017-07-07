# - * - coding:utf8 - * - -
###########################################
# Author: Tinkle
# E-mail: shutingnupt@gmail.com
# Name:  Minimum Path Sum.py
# Creation Time: 2017/7/7
###########################################
'''
Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.

'''
class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if i==0 and j==0:
                    grid[i][j]=grid[i][j]
                elif i==0:
                    grid[i][j]=grid[i][j-1]+grid[i][j]
                elif j==0:
                    grid[i][j]=grid[i-1][j]+grid[i][j]
                else:
                    grid[i][j]= min(grid[i-1][j],grid[i][j-1])+grid[i][j]
        return grid[-1][-1]