# - * - coding:utf8 - * - -
###########################################
# Author: Tinkle
# E-mail: shutingnjupt@gmail.com
# Name:  Game of Life.py
# Creation Time: 2017/8/28
###########################################
'''
According to the Wikipedia's article: "The Game of Life, also known simply as Life, is a cellular automaton devised by the British mathematician John Horton Conway in 1970."

Given a board with m by n cells, each cell has an initial state live (1) or dead (0). Each cell interacts with its eight neighbors (horizontal, vertical, diagonal) using the following four rules (taken from the above Wikipedia article):

Any live cell with fewer than two live neighbors dies, as if caused by under-population.
Any live cell with two or three live neighbors lives on to the next generation.
Any live cell with more than three live neighbors dies, as if by over-population..
Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
Write a function to compute the next state (after one update) of the board given its current state.

Follow up:
Could you solve it in-place? Remember that the board needs to be updated at the same time: You cannot update some cells first and then use their updated values to update other cells.
In this question, we represent the board using a 2D array. In principle, the board is infinite, which would cause problems when the active area encroaches the border of the array. How would you address these problems?

'''
class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        m=len(board)
        if m:
            n=len(board[0])
        def Sumscore(i,j,board,m,n):
            ans=0
            if i!=0:  #up
                ans=ans+board[i-1][j]
                if j!=0: #left up
                    ans=ans+board[i-1][j-1]
            if j!=0:  #left
                ans=ans+board[i][j-1]
                if i!=(m-1): #left down
                    ans=ans+board[i+1][j-1]
            if i!=(m-1): #down
                ans=ans+board[i+1][j]
                if j!=(n-1): #right down
                    ans=ans+board[i+1][j+1]
            if j!=(n-1): #right
                ans=ans+board[i][j+1]
                if i!=0: #right up
                    ans=ans+board[i-1][j+1]
            return ans
        state=[[0 for i in range(n)] for j in range(m)]
        for i in range(m):
            for j in range(n):
                tmp=Sumscore(i,j,board,m,n)
                if board[i][j]:
                    if tmp==2 or tmp==3:
                        state[i][j]=1
                    else:
                        state[i][j]=0
                else:
                    if tmp==3:
                        state[i][j]=1
                    else:
                        state[i][j]=0
        for i in range(m):
            for j in range(n):
                board[i][j]=state[i][j]