# - * - coding:utf8 - * - -
###########################################
# Author: Tinkle
# E-mail: shutingnjupt@gmail.com
# Name:  Best Time to Buy and Sell Stock IV.py
# Creation Time: 2018/3/10
###########################################
'''
class Solution(object):
    def maxProfit(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """
        if prices == [] or k ==0 : return 0
        size = len(prices)
        if k>(size/2): return self.maxProfit1(prices)
        L = [[0 for i in range(k+1)] for p in prices]
        G = [[0 for i in range(k+1)] for p in prices]
        for j in range(1,k+1):
            for i in range(1,len(prices)):
                diff = prices[i]-prices[i-1]
                L[i][j] = max(G[i-1][j-1],G[i-1][j-1]+diff,L[i-1][j]+diff)
                G[i][j] = max(G[i-1][j],L[i][j])
        return G[len(prices)-1][k]

    def maxProfit1(self, prices):
        if prices == []: return 0
        ans = 0
        for i in range(1,len(prices)):
            diff = prices[i]-prices[i-1]
            if diff>0:  ans+=diff
        return ans
'''


class Solution(object):
    def maxProfit(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """
        if prices == [] or k == 0: return 0
        size = len(prices)
        if k > (size / 2): return self.maxProfit1(prices)
        L = [[0 for i in range(k + 1)] for p in prices]
        G = [[0 for i in range(k + 1)] for p in prices]
        for j in range(1, k + 1):
            for i in range(1, len(prices)):
                diff = prices[i] - prices[i - 1]
                L[i][j] = max(G[i - 1][j - 1], G[i - 1][j - 1] + diff, L[i - 1][j] + diff)
                G[i][j] = max(G[i - 1][j], L[i][j])
        return G[len(prices) - 1][k]

    def maxProfit1(self, prices):
        if prices == []: return 0
        ans = 0
        for i in range(1, len(prices)):
            diff = prices[i] - prices[i - 1]
            if diff > 0:  ans += diff
        return ans