# - * - coding:utf8 - * - -
###########################################
# Author: Tinkle
# E-mail: shutingnupt@gmail.com
# Name:  Unique PathsII.py
# Creation Time: 2017/7/7
###########################################
'''
Follow up for "Unique Paths":

Now consider if some obstacles are added to the grids. How many unique paths would there be?

An obstacle and empty space is marked as 1 and 0 respectively in the grid.

For example,
There is one obstacle in the middle of a 3x3 grid as illustrated below.

[
  [0,0,0],
  [0,1,0],
  [0,0,0]
]
'''
class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        m=len(obstacleGrid)
        n=len(obstacleGrid[0])
        num=[]
        for i in range(m):
            num.append([])
            for j in range(n):
                if obstacleGrid[i][j]==1:
                    num[i].append(0)
                elif i==0 and j==0:
                    num[i].append(1)
                elif i==0:
                    num[i].append(num[i][j-1])
                elif j==0:
                    num[i].append(num[i-1][j])
                else:
                    num[i].append(num[i][j-1]+num[i-1][j])
        return num[m-1][n-1]