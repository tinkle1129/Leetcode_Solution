# - * - coding:utf8 - * - -
###########################################
# Author: Tinkle
# E-mail: shutingnjupt@gmail.com
# Name: Number of Islands
# Creation Time: 2017/8/13
###########################################
'''
Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

Example 1:

11110
11010
11000
00000
Answer: 1

Example 2:

11000
11000
00100
00011
Answer: 3
'''
class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if len(grid) == 0:
            return 0
        ret = 0
        dx = [-1,1,0,0]
        dy = [0,0,-1,1]
        visited = [[False for i in range(len(grid[0]))] for j in range(len(grid))]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if visited[i][j]:
                    continue
                visited[i][j] = True
                if grid[i][j] == '1':
                    stack = [(i,j)]
                    while(len(stack)):
                        pos = stack.pop()
                        for k in range(4):
                            new_x = pos[0]+dx[k]
                            new_y = pos[1]+dy[k]
                            if new_x>=0 and new_x<len(grid) and new_y>=0 and new_y<len(grid[0]) and visited[new_x][new_y]==False and grid[new_x][new_y]=='1':
                                stack.append((new_x,new_y))
                                visited[new_x][new_y] =True
                    ret+=1
        return ret
S = Solution()
print S.numIslands([['1','1','1','1','0'],
['1','1','0','1','0'],
['1','1','0','0','0'],
['0','0','0','0','0']])
print S.numIslands([['1','1','0','0','0'],
['1','1','0','0','0'],
['0','0','1','0','0'],
['0','0','0','1','1']])
