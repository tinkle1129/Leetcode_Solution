# - * - coding:utf8 - * - -
###########################################
# Author: Tinkle
# E-mail: shutingnjupt@gmail.com
# Name:Reverse String.py
# Creation Time: 2017/9/6
###########################################
'''
Write a function that takes a string as input and returns the string reversed.

Example:
Given s = "hello", return "olleh".


'''
class Solution(object):
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = list(s)
        start = 0
        end = len(s)-1
        while(start<end):
            s[start],s[end] = s[end],s[start]
            start+=1
            end-=1
        return ''.join(s)