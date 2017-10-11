# - * - coding:utf8 - * - -
###########################################
# Author: Tinkle
# E-mail: shutingnjupt@gmail.com
# Name: Reconstruct Original Digits from English.py
# Creation Time: 2017/10/11
###########################################
'''
Given a non-empty string containing an out-of-order English representation of digits 0-9, output the digits in ascending order.

Note:
Input contains only lowercase English letters.
Input is guaranteed to be valid and can be transformed to its original digits. That means invalid inputs such as "abc" or "zerone" are not permitted.
Input length is less than 50,000.
Example 1:
Input: "owoztneoer"

Output: "012"
Example 2:
Input: "fviefuro"

Output: "45"
'''

import collections
class Solution(object):
    def originalDigits(self, s):
        """
        :type s: str
        :rtype: str
        """
        dic = collections.defaultdict(int)
        map_dic = {'zero':'0','one':'1','two':'2','three':'3','four':'4',
                   'five':'5','six':'6','seven':'7','eight':'8','nine':'9'}
        for i in s:
            dic[i]+=1

        ret = []
        wordlist= [{'zero':'z','two':'w','four':'u','six':'x','eight':'g'},
                   {'one': 'o', 'three': 't', 'five': 'f', 'seven': 's'},
                   {'nine':'i'}]
        for worddic in wordlist:
            for word in worddic:
                cnt = dic[worddic[word]]
                for w in word:
                    dic[w]-=cnt
                ret+=[map_dic[word]]*cnt
        return ''.join(sorted(ret))

S = Solution()
print S.originalDigits("fviefuro")


