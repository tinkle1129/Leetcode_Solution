# - * - coding:utf8 - * - -
###########################################
# Author: Tinkle
# E-mail: shutingnjupt@gmail.com
# Name:   Excel Sheet Column Number.py
# Creation Time: 2018/3/22
###########################################
class Solution(object):
    def titleToNumber(self, s):
        Array_=list(s)
        Array_.reverse()
        s=0
        for i in range(len(Array_)):
            s+=(ord(Array_[i])-ord('A')+1)*(26**i)
        return s
