# - * - coding:utf8 - * - -
###########################################
# Author: Tinkle
# E-mail: shutingnjupt@gmail.com
# Name: Reverse Vowels of a String.py
# Creation Time: 2017/9/8
###########################################
'''
Write a function that takes a string as input and reverse only the vowels of a string.

Example 1:
Given s = "hello", return "holle".

Example 2:
Given s = "leetcode", return "leotcede".

Note:
The vowels does not include the letter "y".
'''
class Solution(object):
    def reverseVowels(self,s):
        dic=['a','o','e','i','u','A','O','E','I','U']
        if s == '':
            return s
        start = 0
        end = len(s)-1
        tmp = list(s)
        while(True):
            while(start<end and tmp[start] not in dic):
                start +=1
            while(start<end and tmp[end] not in dic):
                end -=1
            if start>=end:
                break
            else:
                t = tmp[start]
                tmp[start] = tmp[end]
                tmp[end] = t
                start+=1
                end -=1
        return ''.join(tmp)

    def reverseVowels_(self, s):
        """
        :type s: str
        :rtype: str
        """
        dic=['a','o','e','i','u','A','O','E','I','U']
        context=[]
        index=[]
        for i in range(len(s)):
            if s[i] in dic:
                context.append(s[i])
                index.append(i)
        context.reverse()
        tmp=list(s)
        for i in range(len(index)):
            tmp[index[i]]=context[i]
        return ''.join(tmp)