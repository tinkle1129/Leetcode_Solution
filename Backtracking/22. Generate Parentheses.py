###########################################
# Author: Tinkle
# E-mail: shutingnupt@gmail.com
# Name: Generate Parentheses.py
# Creation Time: 2017/6/25
###########################################
'''
Given n pairs of parentheses,
write a function to generate all combinations of well-formed parentheses.

For example, given n = 3, a solution set is:

[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]
'''
class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        dp = {0:[''],1:['()']}
        def dfs(n):
            if n not in dp:
                dp[n]=[]
                for i in range(n):
                    for inner in dfs(i):
                        for outter in dfs(n-i-1):
                            dp[n].append('('+inner+')'+outter)
            return dp[n]
        return dfs(n)

S = Solution()
print S.generateParenthesis(3)