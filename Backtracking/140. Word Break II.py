# - * - coding:utf8 - * - -
###########################################
# Author: Tinkle
# E-mail: shutingnjupt@gmail.com
# Name: Word Break II.py
# Creation Time: 2017/7/26
###########################################
'''
Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, add spaces in s to construct a sentence where each word is a valid dictionary word. You may assume the dictionary does not contain duplicate words.

Return all such possible sentences.

For example, given
s = "catsanddog",
dict = ["cat", "cats", "and", "sand", "dog"].

A solution is ["cats and dog", "cat sand dog"].
'''


class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        worddict = {}
        for word in wordDict:
            worddict[word] = True
        dp = [True] + [False for i in s]
        star = [[] for i in range(len(s)+1)]
        for i in range(len(s)):
            for j in range(i + 1):
                if s[j:i + 1] in worddict and dp[j] == True:
                    dp[i + 1] = True
                    star[i+1].append(j)
        ret = []
        def backtacking(lastptr,tmp):
            if lastptr == 0:
                ret.append(tmp)
            else:
                for curptr in star[lastptr]:
                    if lastptr == -1:
                        newtmp = s[curptr:]
                    else:
                        newtmp = s[curptr:lastptr] + ' ' + tmp
                    backtacking(curptr,newtmp)

        if dp[-1]:
            backtacking(-1,'')
        return ret

S = Solution()
print S.wordBreak("catsanddog",
["cat","cats","and","sand","dog"])
print S.wordBreak('aaa',['a','aa','aaa'])