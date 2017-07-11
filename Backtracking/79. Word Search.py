# - * - coding:utf8 - * - -
###########################################
# Author: Tinkle
# E-mail: shutingnupt@gmail.com
# Name: Word Search.py
# Creation Time: 2017/7/11
###########################################
'''
Given a 2D board and a word, find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once.

For example,
Given board =

[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]
word = "ABCCED", -> returns true,
word = "SEE", -> returns true,
word = "ABCB", -> returns false.
'''
class Solution(object):
    def dfs(self,x,y,step,word,board):
        if step==len(word):
            return True
        dx=[1,-1,0, 0]
        dy=[0, 0,1,-1]
        for k in range(4):
            fx = x+dx[k]
            fy = y+dy[k]
            if(fx<0 or fx>=len(board) or fy<0 or fy>=len(board[0]) or board[fx][fy]!=word[step]):
                continue
            tmp = board[fx][fy]
            board[fx][fy] = '#'
            if self.dfs(fx,fy,step+1,word,board):
                return True
            board[fx][fy] = tmp
        return False

    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        if not len(word):
            return True

        dx=[1,-1,0, 0]
        dy=[0, 0,1,-1]


        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j]==word[0]:
                    tmp = board[i][j]
                    board[i][j] = '1'
                    if self.dfs(i, j, 1, word, board):
                        return True
                    board[i][j]=tmp

        return False