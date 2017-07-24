# - * - coding:utf8 - * - -
###########################################
# Author: Tinkle
# E-mail: shutingnjupt@gmail.com
# Name: Surrounded Regions.py
# Creation Time: 2017/7/24
###########################################
'''
Given a 2D board containing 'X' and 'O' (the letter O), capture all regions surrounded by 'X'.

A region is captured by flipping all 'O's into 'X's in that surrounded region.

For example,
X X X X
X O O X
X X O X
X O X X
After running your function, the board should be:

X X X X
X X X X
X X X X
X O X X
'''


class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        if len(board)==0:
            return
        visits = [[True for i in board[0]] for j in board]
        m  = len(board)
        n = len(board[0])
        for i in range(m):
            for j in range(n):
                if visits[i][j] and board[i][j]=='O':
                    candidates = []
                    visits[i][j]=False
                    candidates.append((i,j))
                    tmp = [(i,j)]
                    dx = [0,0,-1,1]
                    dy = [-1,1,0,0]
                    max_x = i
                    min_x = i
                    max_y = j
                    min_y = j
                    while(len(tmp)):
                        for k in range(4):
                            tmp_x = tmp[0][0]+dx[k]
                            tmp_y = tmp[0][1]+dy[k]
                            if tmp_x>=0 and tmp_x<m and tmp_y>=0 and tmp_y<n:
                                if board[tmp_x][tmp_y] == 'O' and visits[tmp_x][tmp_y]:
                                    max_x = max(max_x,tmp_x)
                                    min_x = min(min_x,tmp_x)
                                    min_y = min(min_y,tmp_y)
                                    max_y = max(max_y,tmp_y)
                                    visits[tmp_x][tmp_y] = False
                                    candidates.append((tmp_x,tmp_y))
                                    tmp.append((tmp_x,tmp_y))
                        tmp.remove(tmp[0])
                    if max_x < m-1 and min_x > 0 and max_y< n-1 and min_y>0:
                        for line in candidates:
                            board[line[0]][line[1]] = 'X'
S = Solution()
boad = [
['X', 'X', 'X', 'X'],
['X', 'O', 'O', 'X'],
['X', 'X', 'O', 'X'],
['X', 'O', 'X', 'X']
]
S.solve(boad)
print boad
