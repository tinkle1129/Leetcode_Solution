# - * - coding:utf8 - * - -
###########################################
# Author: Tinkle
# E-mail: shutingnjupt@gmail.com
# Name:  Perfect Squares.py
# Creation Time: 2017/8/26
###########################################
'''
Given a positive integer n, find the least number of perfect square numbers (for example, 1, 4, 9, 16, ...) which sum to n.

For example, given n = 12, return 3 because 12 = 4 + 4 + 4; given n = 13, return 2 because 13 = 4 + 9.
'''
class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [i for i in range(n+1)]
        for i in range(n+1):
            j=1
            while(i+j*j<=n):
                dp[i+j*j] = min(dp[i+j*j],dp[i]+1)
                j +=1
        #print dp
        return dp[n]

S = Solution()
print S.numSquares(100)
