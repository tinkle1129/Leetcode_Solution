# - * - coding:utf8 - * - -
###########################################
# Author: Tinkle
# E-mail: shutingnjupt@gmail.com
# Name: Word Ladder.py
# Creation Time: 2017/7/22
###########################################
'''
Given two words (beginWord and endWord), and a dictionary's word list, find the length of shortest transformation sequence from beginWord to endWord, such that:

Only one letter can be changed at a time.
Each transformed word must exist in the word list. Note that beginWord is not a transformed word.
For example,

Given:
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log","cog"]
As one shortest transformation is "hit" -> "hot" -> "dot" -> "dog" -> "cog",
return its length 5.
'''


class Solution:
    def ladderLength(self, start, end, wordList):
        '''
        :param beginWord: str
        :param endWord: str
        :param wordList: list[str]
        :return: int
        '''
        dict = set(wordList)
        wordLen = len(start)
        candidates = set()
        candidates.add((start,1))
        while(True):
            if len(candidates)==0:
                break
            current = set()
            for cur in candidates:
                curWord = cur[0];curLen = cur[1]
                if curWord == end:
                    return curLen
                for i in range(wordLen):
                    left = curWord[:i]
                    right = curWord[i+1:]
                    for j in 'abcdefghijklmnopqrstuvwxyz':
                        if curWord[i]!=j:
                            nextWord = left+j+right
                            if nextWord in dict:
                                if nextWord == end:
                                    return curLen+1
                                current.add((nextWord,curLen+1))
                                dict.remove(nextWord)
            candidates = current
        return 0
S = Solution()
print S.ladderLength('hit','cog',["hot","dot","dog","lot","log","cog"])


