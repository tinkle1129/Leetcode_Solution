# - * - coding:utf8 - * - -
###########################################
# Author: Tinkle
# E-mail: shutingnjupt@gmail.com
# Name: Maximum Product of Word Lengths.py
# Creation Time: 2017/9/1
###########################################
'''
Given a string array words, find the maximum value of length(word[i]) * length(word[j]) where the two words do not share common letters. You may assume that each word will contain only lower case letters. If no such two words exist, return 0.

Example 1:
Given ["abcw", "baz", "foo", "bar", "xtfn", "abcdef"]
Return 16
The two words can be "abcw", "xtfn".

Example 2:
Given ["a", "ab", "abc", "d", "cd", "bcd", "abcd"]
Return 4
The two words can be "ab", "cd".

Example 3:
Given ["a", "aa", "aaa", "aaaa"]
Return 0
'''
class Solution(object):
    def maxProduct(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        ans=[]
        for i in words:
            tmp=0
            for j in set(i):
                tmp=tmp+(1<<(ord(j)-ord('a')))
            ans.append(tmp)
        MAX_P=0
        for i in range(len(words)):
            for j in range(i,len(words)):
                if ans[i] & ans[j]==0:
                    MAX_P=max(MAX_P,len(words[i])*len(words[j]))
        return int(MAX_P)

S = Solution()
print S.maxProduct(["a", "aa", "aaa", "aaaa"])