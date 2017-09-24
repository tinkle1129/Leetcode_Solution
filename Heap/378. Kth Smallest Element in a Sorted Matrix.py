# - * - coding:utf8 - * - -
###########################################
# Author: Tinkle
# E-mail: shutingnjupt@gmail.com
# Name: Kth Smallest Element in a Sorted Matrix.py
# Creation Time: 2017/9/22
###########################################
'''
Given a n x n matrix where each of the rows and columns are sorted in ascending order, find the kth smallest element in the matrix.

Note that it is the kth smallest element in the sorted order, not the kth distinct element.

Example:

matrix = [
   [ 1,  5,  9],
   [10, 11, 13],
   [12, 13, 15]
],
k = 8,

return 13.
'''

import heapq
class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        m, n = len(matrix), len(matrix[0])
        visited = [[False for j in range(n)] for i in range(m)]
        heap = []
        item = None
        heapq.heappush(heap,(matrix[0][0],0,0))
        for i in range(k):
            item,i,j = heapq.heappop(heap)
            if i+1<m and visited[i+1][j]!=True:
                heapq.heappush(heap,(matrix[i+1][j],i+1,j))
                visited[i+1][j]=True
            if j+1<n and visited[i][j+1]!=True:
                heapq.heappush(heap,(matrix[i][j+1],i,j+1))
                visited[i][j+1]=True
        return item
