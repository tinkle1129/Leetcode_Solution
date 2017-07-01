###########################################
# Author: Tinkle
# E-mail: shutingnupt@gmail.com
# Name:  Substring with Concatenation of All Words.py
# Creation Time: 2017/7/1
###########################################
'''
You are given a string, s, and a list of words, words, that are all of the same length. Find all starting indices of substring(s) in s that is a concatenation of each word in words exactly once and without any intervening characters.

For example, given:
s: "barfoothefoobarman"
words: ["foo", "bar"]

You should return the indices: [0,9].
'''


class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        ind = []
        length = len(words[0])
        count = len(words)
        word_dict = {}
        for word in words:
            word_dict.setdefault(word,0)
            word_dict[word]+=1
        for i in range(len(s)+1-length*count):

            idx = i
            cnt = 0
            wordd ={}
            #print idx
            while(cnt<count):
                word = s[idx:idx+length]
                if word not in words:
                    break
                else:
                    wordd.setdefault(word,0)
                    wordd[word]+=1
                if wordd[word]>word_dict[word]:
                    break
                cnt +=1
                idx = idx+length
            if cnt == count:
                ind.append(i)
        return ind

S = Solution()
print S.findSubstring("wordgoodgoodgoodbestword",["word","good","best","good"])
print S.findSubstring("barfoothefoobarman",["foo","bar"])