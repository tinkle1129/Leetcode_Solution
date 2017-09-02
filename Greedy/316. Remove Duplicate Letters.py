# - * - coding:utf8 - * - -
###########################################
# Author: Tinkle
# E-mail: shutingnjupt@gmail.com
# Name:  Remove Duplicate Letters.py
# Creation Time: 2017/9/1
###########################################
'''
Given a string which contains only lowercase letters, remove duplicate letters so that every letter appear once and only once. You must make sure your result is the smallest in lexicographical order among all possible results.

Example:
Given "bcabc"
Return "abc"

Given "cbacdcbc"
Return "acdb"
'''


class Solution(object):
    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        keydict = {}
        for t in s:
            keydict.setdefault(t,0)
            keydict[t]+=1
        stack = []
        for t in s:
            keydict[t]-=1
            if t not in stack:
                while stack and stack[-1]>t and keydict[stack[-1]]>0:
                    stack.pop()
                stack.append(t)
        return ''.join(stack)
S = Solution()
print S.removeDuplicateLetters("bcabc")
