# - * - coding:utf8 - * - -
###########################################
# Author: Tinkle
# E-mail: shutingnjupt@gmail.com
# Name: First Unique Character in a String.py
# Creation Time: 2017/9/24
###########################################
'''
Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.

Examples:

s = "leetcode"
return 0.

s = "loveleetcode",
return 2.
'''


class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        dic = {}
        for i in range(len(s)):
            dic.setdefault(s[i], [])
            dic[s[i]] += [i]
        minidx = len(s)
        for item in dic:
            if len(dic[item]) == 1:
                minidx = min(minidx, dic[item][0])
        return minidx if minidx != len(s) else -1

