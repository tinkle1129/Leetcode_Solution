# - * - coding:utf8 - * - -
###########################################
# Author: Tinkle
# E-mail: shutingnjupt@gmail.com
# Name:  Best Time to Buy and Sell Stock III.py
# Creation Time: 2018/3/10
###########################################
'''
Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete at most two transactions.

Note:
You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).

Seen this question in a real interview before?

'''
class Solution(object):
    def maxProfit(self,prices):
        if prices == []: return 0
        size = len(prices)
        MIN,MAX = prices[0],prices[size-1]
        prev,post = [0],[0]
        for i in range(1,size):
            x = prices[i]
            y = prices[size-1-i]
            MAX,MIN = max(MAX,y),min(MIN,x)
            prev.append(max(prev[-1],x-MIN))
            post.append(max(post[-1],MAX-y))
        post.reverse()
        ret = 0
        for i in range(size):
            ret = max(ret,prev[i]+post[i])
        return ret