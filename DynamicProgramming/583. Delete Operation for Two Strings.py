# - * - coding:utf8 - * - -
###########################################
# Author: Tinkle
# E-mail: shutingnupt@gmail.com
# Name:   Delete Operation for Two Strings.py
# Creation Time: 2018/3/14
###########################################
'''
Given two words word1 and word2, find the minimum number of steps required to make word1 and word2 the same, where in each step you can delete one character in either string.

Example 1:
Input: "sea", "eat"
Output: 2
Explanation: You need one step to make "sea" to "ea" and another step to make "eat" to "ea".
Note:
The length of given words won't exceed 500.
Characters in given words can only be lower-case letters.
'''


class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        l1,l2 = len(word1),len(word2)
        dp = [[0 for i in range(l2+1)] for j in range(l1+1)]
        for i in range(l1+1):
            for j in range(l2+1):
                if i==0 or j==0:
                    dp[i][j] = i+j
                elif word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = min(dp[i-1][j],dp[i][j-1])+1
        return dp[l1][l2]
    
S = Solution()
print S.minDistance("sea", "eat")
