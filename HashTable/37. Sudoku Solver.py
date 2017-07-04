# - * - coding:utf8 - * - -
###########################################
# Author: Tinkle
# E-mail: shutingnupt@gmail.com
# Name:  Sudoku Solver.py
# Creation Time: 2017/7/2
###########################################
'''
Write a program to solve a Sudoku puzzle by filling the empty cells.

Empty cells are indicated by the character '.'.

You may assume that there will be only one unique solution.
'''

class Solution(object):

    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        def isValid(x,y):
            tmp = board[x][y]
            board[x][y] = '.'
            for i in range(9):
                if board[i][y] == tmp:
                    return False
            for j in range(9):
                if board[x][j] == tmp:
                    return False
            for i in range(3):
                for j in range(3):
                    if board[(x/3)*3+i][(y/3)*3+j] == tmp:
                        return False
            board[x][y] = tmp
            return True
        def dfs(board):
            for i in range(9):
                for j in range(9):
                    if board[i][j]=='.':
                        for k in '123456789':
                            board[i][j]=k
                            if isValid(i,j) and dfs(board):
                                return True
                            board[i][j]='.'
                        return False
            return True
        dfs(board)
