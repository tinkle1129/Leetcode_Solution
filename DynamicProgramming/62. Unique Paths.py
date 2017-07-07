# - * - coding:utf8 - * - -
###########################################
# Author: Tinkle
# E-mail: shutingnupt@gmail.com
# Name:  Unique Paths.py
# Creation Time: 2017/7/7
###########################################
'''
A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

How many possible unique paths are there?
'''
class Solution(object):
    def uniquePaths(self, m, n):
        '''
        :param m: int
        :param n: int
        :return: int
        '''
        ret = []
        for i in range(m):
            ret.append([])
            for j in range(n):
                if i==0 or j==0:
                    ret[i].append(1)
                else:
                    ret[i].append(ret[i-1][j]+ret[i][j-1])
        return ret[m-1][n-1]