# - * - coding:utf8 - * - -
###########################################
# Author: Tinkle
# E-mail: shutingnjupt@gmail.com
# Name: Is Subsequence.py
# Creation Time: 2017/9/25
###########################################
'''
Given a string s and a string t, check if s is subsequence of t.

You may assume that there is only lower case English letters in both s and t. t is potentially a very long (length ~= 500,000) string, and s is a short string (<=100).

A subsequence of a string is a new string which is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (ie, "ace" is a subsequence of "abcde" while "aec" is not).

Example 1:
s = "abc", t = "ahbgdc"

Return true.

Example 2:
s = "axc", t = "ahbgdc"

Return false.
'''


class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        pos_s = 0
        pos_t = 0
        while(pos_s<len(s) and pos_t<len(t)):
            if s[pos_s]==t[pos_t]:
                pos_t+=1
                pos_s+=1
            else:
                pos_t+=1
        return pos_s==len(s)
S = Solution()
print S.isSubsequence('abc','ahbgdc')
print S.isSubsequence('axc','ahbgdc')