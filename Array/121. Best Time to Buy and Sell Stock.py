###########################################
# Author: Tinkle
# E-mail: shutingnupt@gmail.com
# Name:  Best Time to Buy and Sell Stock.py
# Creation Time: 2018/1/22
###########################################
'''
Say you have an array for which the ith element is the price of a given stock on day i.

If you were only permitted to complete at most one transaction (ie, buy one and sell one share of the stock), design an algorithm to find the maximum profit.

Example 1:
Input: [7, 1, 5, 3, 6, 4]
Output: 5

max. difference = 6-1 = 5 (not 7-1 = 6, as selling price needs to be larger than buying price)
Example 2:
Input: [7, 6, 4, 3, 1]
Output: 0

In this case, no transaction is done, i.e. max profit = 0.
'''
import sys
MAX_=sys.maxint
class Solution(object):
    def maxProfit(self, prices):
        if not len(prices):
            return 0
        MIN=MAX_
        values=[]
        for i in range(len(prices)):
            MIN=min(MIN,prices[i])
            values.append(prices[i]-MIN)
        return max(values)