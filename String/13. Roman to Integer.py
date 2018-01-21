# - * - coding:utf8 - * - -
###########################################
# Author: Tinkle
# E-mail: shutingnjupt@gmail.com
# Name: Roman to Integer.py
# Creation Time: 2017/1/21
###########################################
'''
Given a roman numeral, convert it to an integer.

Input is guaranteed to be within the range from 1 to 3999.
'''
class Solution(object):
    def romanToInt(self,s):
        '''
        :param s: str
        :return: int
        '''
        if len(s)==0:
            return 0
        d = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        ret = 0
        tmp = d[s[0]]
        for i in range(1,len(s)):
            if d[s[i]]<d[s[i-1]]:
                ret +=tmp
                tmp = 0
            elif d[s[i]] > d[s[i-1]]:
                ret -=tmp
                tmp = 0
            tmp +=d[s[i]]
        ret +=tmp
        return ret