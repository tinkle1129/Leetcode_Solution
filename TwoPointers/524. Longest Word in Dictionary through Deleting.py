###########################################
# Author: Tinkle
# E-mail: shutingnupt@gmail.com
# Name:  Longest Word in Dictionary through Deleting.py
# Creation Time: 2018/4/18
###########################################
'''
Given a string and a string dictionary, find the longest string in the dictionary that can be formed by deleting some characters of the given string. If there are more than one possible results, return the longest word with the smallest lexicographical order. If there is no possible result, return the empty string.

Example 1:
Input:
s = "abpcplea", d = ["ale","apple","monkey","plea"]

Output:
"apple"
Example 2:
Input:
s = "abpcplea", d = ["a","b","c"]

Output:
"a"
Note:
All the strings in the input will only contain lower-case letters.
The size of the dictionary won't exceed 1,000.
The length of all the strings in the input won't exceed 1,000.
'''


class Solution(object):
    def findLongestWord(self, s, d):
        """
        :type s: str
        :type d: List[str]
        :rtype: str
        """
        maxlen = [len(token) for token in d]
        pos = [0 for token in d]
        ret = []
        for token in s:
            for i in range(len(pos)):
                if pos[i] < maxlen[i] and d[i][pos[i]] == token:
                    pos[i] += 1
                    if pos[i] == maxlen[i]:
                        ret.append(d[i])
        if ret == []: return ''
        maxl = len(max(ret, key=len))
        return min(w for w in ret if len(w) == maxl)
