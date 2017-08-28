# - * - coding:utf8 - * - -
###########################################
# Author: Tinkle
# E-mail: shutingnjupt@gmail.com
# Name:  Word Pattern.py
# Creation Time: 2017/8/28
###########################################
'''
Given a pattern and a string str, find if str follows the same pattern.

Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in str.

Examples:
pattern = "abba", str = "dog cat cat dog" should return true.
pattern = "abba", str = "dog cat cat fish" should return false.
pattern = "aaaa", str = "dog cat cat dog" should return false.
pattern = "abba", str = "dog dog dog dog" should return false.
'''


class Solution(object):
    def wordPattern(self, pattern, str):
        temp=str.split()
        table={}
        flag=1
        if len(temp)!=len(pattern):
            return False
        for i in range(len(pattern)):
            table.setdefault(pattern[i],None)
            if table[pattern[i]]==None:
                for k in table:
                    if k!=pattern[i]:
                        if temp[i]==table[k]:
                            return False
                    table[pattern[i]]=temp[i]
            elif temp[i]!=table[pattern[i]]:
                return False
        if flag:
            return True

S = Solution()
print S.wordPattern("abba","dog cat cat fish")