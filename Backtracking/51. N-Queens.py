# - * - coding:utf8 - * - -
###########################################
# Author: Tinkle
# E-mail: shutingnupt@gmail.com
# Name: N-Queens.py
# Creation Time: 2017/7/4
###########################################
'''
The n-queens puzzle is the problem of placing n queens on an n×n chessboard such that no two queens attack each other.

Given an integer n, return all distinct solutions to the n-queens puzzle.

Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a queen and an empty space respectively.


'''
class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        digit = [['.' for x in range(n)] for j in range(n)]
        ret = []
        def Queens(digit, step):
            if step == n:
                ans = [''.join(digit[i]) for i in range(n)]
                ret.append(ans)
            else:
                for i in range(n):
                    digit[step][i] = 'Q'
                    flag = 0
                    for x in range(step):
                        for j in range(n):
                            if not (x==step and i==j):
                                if digit[x][j] == 'Q':
                                    if (x == step or j == i or abs(step - x) == abs(i - j)):
                                        flag = 1
                                        break
                    if flag == 0:
                        Queens(digit, step + 1)
                    digit[step][i] = '.'
        Queens(digit,0)
        return ret