###########################################
# Author: Tinkle
# E-mail: shutingnupt@gmail.com
# Name: Longest Substring Without Repeating Characters.py
# Creation Time: 2017/6/20
###########################################
'''
Given a string, find the length of the longest substring without repeating characters.

Examples:

Given "abcabcbb", the answer is "abc", which the length is 3.

Given "bbbbb", the answer is "b", with the length of 1.

Given "pwwkew", the answer is "wke", with the length of 3. Note that the answer must be a substring, "pwke" is a subsequence and not a substring.

'''
class Solution(object):
    def lengthOfLongestSubstring(self,s):
        '''
        :param s: str
        :return: int
        '''
        if len(s)==0:
            return 0
        hashtable = {}
        s_pointer = 0
        e_pointer = 0
        maxlen = 0
        for i in range(len(s)):
            if s[i] not in hashtable:
                hashtable.setdefault(s[i],i)
                e_pointer = i
            else:
                if hashtable[s[i]]< s_pointer:
                    hashtable[s[i]] = i
                    e_pointer = i
                else:
                    maxlen = max(e_pointer-s_pointer+1,maxlen)
                    s_pointer = hashtable[s[i]]+1
                    hashtable[s[i]] = i
                    e_pointer = i
        return max(e_pointer-s_pointer+1,maxlen)

S = Solution()
print S.lengthOfLongestSubstring('pwwkew')