# - * - coding:utf8 - * - -
###########################################
# Author: Tinkle
# E-mail: shutingnjupt@gmail.com
# Name:  Coin Change.py
# Creation Time: 2017/9/2
###########################################
'''
You are given coins of different denominations and a total amount of money amount. Write a function to compute the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

Example 1:
coins = [1, 2, 5], amount = 11
return 3 (11 = 5 + 5 + 1)

Example 2:
coins = [2], amount = 3
return -1.

Note:
You may assume that you have an infinite number of each kind of coin.

'''
import sys
MAX_=sys.maxint
class Solution(object):
    def coinChange(self, coins, amount):
        if not len(coins):
            return -1
        if amount<=0:
            return 0
        dp=[MAX_ for i in range(1,amount+1)]
        dp.insert(0,0)
        for id in range(1,amount+1):
            for j in coins:
                if id>=j:
                    diff=id-j
                    if dp[diff]!=MAX_:
                        dp[id]=min(dp[diff]+1,dp[id])
        if dp[amount]==MAX_:
            return -1
        else:
            return dp[amount]