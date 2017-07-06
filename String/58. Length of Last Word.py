# - * - coding:utf8 - * - -
###########################################
# Author: Tinkle
# E-mail: shutingnupt@gmail.com
# Name:  Length of Last Word.py
# Creation Time: 2017/7/6
###########################################
'''
Given a string s consists of upper/lower-case alphabets and empty space characters ' ', return the length of last word in the string.

If the last word does not exist, return 0.

Note: A word is defined as a character sequence consists of non-space characters only.

For example,
Given s = "Hello World",
return 5.
'''


class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s == '':
            return 0
        x = 0
        for i in range(len(s)):
            if s[i] != ' ':
                if i == 0 or s[i - 1] == ' ':
                    x = 1
                else:
                    x += 1
        return x
