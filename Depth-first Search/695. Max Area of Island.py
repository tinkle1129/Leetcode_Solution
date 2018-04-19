# - * - coding:utf8 - * - -
###########################################
# Author: Tinkle
# E-mail: shutingnjupt@gmail.com
# Name: Max Area of Island.py
# Creation Time: 2018/4/7
###########################################
'''
Given a non-empty 2D array grid of 0's and 1's, an island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.

Find the maximum area of an island in the given 2D array. (If there is no island, the maximum area is 0.)

Example 1:
[[0,0,1,0,0,0,0,1,0,0,0,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,1,1,0,1,0,0,0,0,0,0,0,0],
 [0,1,0,0,1,1,0,0,1,0,1,0,0],
 [0,1,0,0,1,1,0,0,1,1,1,0,0],
 [0,0,0,0,0,0,0,0,0,0,1,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,0,0,0,0,0,0,1,1,0,0,0,0]]
Given the above grid, return 6. Note the answer is not 11, because the island must be connected 4-directionally.
Example 2:
[[0,0,0,0,0,0,0,0]]
Given the above grid, return 0.
Note: The length of each dimension in the given grid does not exceed 50.
'''


class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        if m == 0: return 0
        n = len(grid[0])
        disvisited = [[True for j in range(n)] for i in range(m)]

        def dfs(ii, jj):
            ret = 0
            dx = [0, 0, -1, 1]
            dy = [1, -1, 0, 0]
            for k in range(4):
                x = ii + dx[k]
                y = jj + dy[k]
                if x >= 0 and x < m and y >= 0 and y < n and disvisited[x][y] and grid[x][y]:
                    disvisited[x][y] = False
                    ret = ret + 1 + dfs(x, y)
            return ret

        maxret = 0
        for i in range(m):
            for j in range(n):
                if disvisited[i][j] and grid[i][j]:
                    disvisited[i][j] = False
                    cnt = 1 + dfs(i, j)
                    maxret = max(maxret, cnt)
        return maxret

S = Solution()
print S.maxAreaOfIsland([[1,1,0,0,0],[1,1,0,0,0],[0,0,0,1,1],[0,0,0,1,1]])