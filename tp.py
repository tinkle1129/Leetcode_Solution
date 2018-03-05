# -*- coding:utf-8 -*-
class Solution:
    def hasPath(self, matrix, rows, cols, path):
        def dfs(memories,r,c,s):
            if s=='':
                return True
            dx = [-1,1,0,0]
            dy = [0,0,-1,1]
            for k in range(4):
                x = dx[k] + r
                y = dy[k] + c
                if x >= 0 and x < rows and y >= 0 and y < cols and memories[x][y] and matrix[x*cols+y]==s[0]:
                    memories[x][y]=False
                    if dfs(memories[:], x, y,s[1:]):
                        return True
                    memories[x][y]=True
            return False

        if path == '':
            return True
        memories = [[True for c in range(cols)] for r in range(rows)]
        for r in range(rows):
            for c in range(cols):
                if matrix[r*cols+c] == path[0]:
                    memories[r][c] = False
                    if dfs(memories[:],r,c,path[1:]):
                        return True
                    memories[r][c] = True
        return False






S = Solution()
print S.hasPath('abcesfcsadee',3,4,'abcced')