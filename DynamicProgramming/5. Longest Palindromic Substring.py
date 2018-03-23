# - * - coding:utf8 - * - -
###########################################
# Author: Tinkle
# E-mail: shutingnupt@gmail.com
# Name:   Longest Palindromic Substring.py
# Creation Time: 2018/3/17
###########################################
'''
Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

Example:

Input: "babad"

Output: "bab"

Note: "aba" is also a valid answer.


Example:

Input: "cbbd"

Output: "bb"
'''
class Solution(object):
    def longestPalindrome(self,s):
        '''
        :param s: str
        :return: str
        '''
        ss = '$';idx=0;mx=0
        for i in s:
            ss = ss+'#'+i
        ss = ss+'#'
        P = [0 for i in range(len(ss))]
        for i in range(1,len(ss)):
            if P[idx]+idx<i:
                P[i] = 1
            else:
                P[i] = min(P[2*idx-i],P[idx]+idx-i)
            while(i+P[i]<len(ss) and ss[i-P[i]]==ss[i+P[i]]):
                P[i] = P[i]+1
            if idx + P[idx] < i + P[i]:
                idx = i
            if P[i]>P[mx]:
                mx = i
        a = ss[mx - (P[mx] - 1):mx + P[mx]]
        ret = ''
        for i in a:
            if i!='#':
                ret+=i
        return ret