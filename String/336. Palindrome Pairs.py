# - * - coding:utf8 - * - -
###########################################
# Author: Tinkle
# E-mail: shutingnjupt@gmail.com
# Name:  Palindrome Pairs.py
# Creation Time: 2017/9/5
###########################################
'''
Given a list of unique words, find all pairs of distinct indices (i, j) in the given list, so that the concatenation of the two words, i.e. words[i] + words[j] is a palindrome.

Example 1:
Given words = ["bat", "tab", "cat"]
Return [[0, 1], [1, 0]]
The palindromes are ["battab", "tabbat"]
Example 2:
Given words = ["abcd", "dcba", "lls", "s", "sssll"]
Return [[0, 1], [1, 0], [3, 2], [2, 4]]
The palindromes are ["dcbaabcd", "abcddcba", "slls", "llssssll"]
'''
class Solution(object):
    def palindromePairs(self, words):
        '''
        :param words: list[str]
        :return: list[list]
        '''
        dict_ = {}
        ret = []
        for i in range(len(words)):
            dict_.setdefault(words[i],i)
        for j in range(len(words)):
            word = words[j]
            for i in range(len(word)+1):
                left = word[:i]
                right = word[i:]
                flag = dict_.get(left[::-1])
                if flag!=None and right == right[::-1] and flag!=j:
                    ret.append([j,flag])
                flag = dict_.get(right[::-1])
                if flag!=None and left == left[::-1] and flag!=j and i!=0:
                    ret.append([flag,j])
        return ret
