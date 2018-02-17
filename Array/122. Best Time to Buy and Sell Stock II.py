###########################################
# Author: Tinkle
# E-mail: shutingnupt@gmail.com
# Name:  Best Time to Buy and Sell Stock.py
# Creation Time: 2018/1/22
###########################################
'''
Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete as many transactions as you like (ie, buy one and sell one share of the stock multiple times). However, you may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).


'''
import sys
MAX_=sys.maxint
class Solution(object):
    def maxProfit(self, prices):
        if not len(prices):
            return 0
        sum=0
        prices.insert(0,MAX_)
        for i in range(1,len(prices)):
            diff=prices[i]-prices[i-1]
            if diff>=0:
                sum=sum+diff
        return sum