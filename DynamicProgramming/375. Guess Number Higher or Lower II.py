# - * - coding:utf8 - * - -
###########################################
# Author: Tinkle
# E-mail: shutingnjupt@gmail.com
# Name: Guess Number Higher or Lower II.py
# Creation Time: 2017/9/21
###########################################
'''
We are playing the Guess Game. The game is as follows:

I pick a number from 1 to n. You have to guess which number I picked.

Every time you guess wrong, I'll tell you whether the number I picked is higher or lower.

However, when you guess a particular number x, and you guess wrong, you pay $x. You win the game when you guess the number I picked.

Example:

n = 10, I pick 8.

First round:  You guess 5, I tell you that it's higher. You pay $5.
Second round: You guess 7, I tell you that it's higher. You pay $7.
Third round:  You guess 9, I tell you that it's lower. You pay $9.

Game over. 8 is the number I picked.

You end up paying $5 + $7 + $9 = $21.
'''


class Solution(object):
    def getMoneyAmount(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [[0 for i in range(n+1)] for j in range(n+1)]
        for gap in range(1, n):
            for lo in range(1, n+1-gap):
                hi = lo + gap
                dp[lo][hi] = min(x + max(dp[lo][x-1], dp[x+1][hi])
                                   for x in range(lo, hi))
        return dp[1][n]

S = Solution()
print S.getMoneyAmount(10)