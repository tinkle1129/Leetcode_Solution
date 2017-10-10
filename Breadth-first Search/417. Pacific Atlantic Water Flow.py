# - * - coding:utf8 - * - -
###########################################
# Author: Tinkle
# E-mail: shutingnjupt@gmail.com
# Name: Partition Equal Subset Sum.py
# Creation Time: 2017/10/10
###########################################
'''
Given an m x n matrix of non-negative integers representing the height of each unit cell in a continent, the "Pacific ocean" touches the left and top edges of the matrix and the "Atlantic ocean" touches the right and bottom edges.

Water can only flow in four directions (up, down, left, or right) from a cell to another one with height equal or lower.

Find the list of grid coordinates where water can flow to both the Pacific and Atlantic ocean.

Note:
The order of returned grid coordinates does not matter.
Both m and n are less than 150.
Example:

Given the following 5x5 matrix:

  Pacific ~   ~   ~   ~   ~
       ~  1   2   2   3  (5) *
       ~  3   2   3  (4) (4) *
       ~  2   4  (5)  3   1  *
       ~ (6) (7)  1   4   5  *
       ~ (5)  1   1   2   4  *
          *   *   *   *   * Atlantic

Return:

[[0, 4], [1, 3], [1, 4], [2, 2], [3, 0], [3, 1], [4, 0]] (positions with parentheses in above matrix).
'''


class Solution(object):
    def pacificAtlantic(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        m = len(matrix)
        if m==0:
            return []
        n = len(matrix[0])


        def bfs(stack,visited,matrix):
            dx = [-1, 1, 0, 0]
            dy = [0, 0, -1, 1]
            ret = set([])
            while(stack):
                item = stack.pop()
                ret.add(item)
                for k in range(4):
                    new_x = item[0]+dx[k]
                    new_y = item[1]+dy[k]
                    if new_x>=0 and new_x<m and new_y>=0 and new_y<n and \
                        visited[new_x][new_y] and matrix[new_x][new_y]>=matrix[item[0]][item[1]]:
                        visited[new_x][new_y]=False
                        stack.append((new_x,new_y))
            return ret

        stack = []
        visited = [[True for j in range(n)] for i in range(m)]
        for i in range(m):
            stack.append((i,0))
            visited[i][0]=False
        for j in range(1,n):
            stack.append((0,j))
            visited[0][j]=False
        Pacific = bfs(stack,visited,matrix)

        stack = []
        visited = [[True for j in range(n)] for i in range(m)]
        for i in range(m):
            stack.append((i, n-1))
            visited[i][n-1] = False
        for j in range(n-1):
            stack.append((m-1, j))
            visited[m-1][j] = False
        Atlantic = bfs(stack,visited,matrix)
        return list(Pacific & Atlantic)




S = Solution()
print S.pacificAtlantic(
    [
        [1,2,2,3,5],
        [3,2,3,4,4],
        [2,4,5,3,1],
        [6,7,1,4,5],
        [5,1,1,2,4]
    ]
)

