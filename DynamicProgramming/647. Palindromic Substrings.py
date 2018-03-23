# - * - coding:utf8 - * - -
###########################################
# Author: Tinkle
# E-mail: shutingnupt@gmail.com
# Name:  Palindromic Substrings.py
# Creation Time: 2018/3/13
###########################################
'''
Given a string, your task is to count how many palindromic substrings in this string.

The substrings with different start indexes or end indexes are counted as different substrings even they consist of same characters.

Example 1:
Input: "abc"
Output: 3
Explanation: Three palindromic strings: "a", "b", "c".
Example 2:
Input: "aaa"
Output: 6
Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".
Note:
The input string length won't exceed 1000.
'''
class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s=='': return 0
        size = len(s)
        dp = [[0 for i in range(size)] for j in range(size)]
        ret = 0
        for i in range(size):
            for j in range(i+1):
                if i==j or (s[i]==s[j] and dp[i-1][j+1]) or (j==i-1 and s[i]==s[j]):
                    dp[i][j] = 1
            ret += sum(dp[i])
        return ret

S = Solution()
print S.countSubstrings('aabba')