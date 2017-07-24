# - * - coding:utf8 - * - -
###########################################
# Author: Tinkle
# E-mail: shutingnjupt@gmail.com
# Name: Palindrome Partitioning.py
# Creation Time: 2017/7/24
###########################################
'''
Given a string s, partition s such that every substring of the partition is a palindrome.

Return all possible palindrome partitioning of s.

For example, given s = "aab",
Return

[
  ["aa","b"],
  ["a","a","b"]
]
'''


class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        def isPalindrome(string):
            start = 0
            end = len(string)-1
            while(start<=end):
                if string[start]!=string[end]:
                    return False
                start +=1
                end -=1
            return True
        if s == '':
            return []
        self.dict_ = {}
        def backtracking(s):
            if len(s)==1:
                return [[s]]
            elif s == '':
                return [[]]
            else:
                ret = []
                for i in range(1,len(s)+1):
                    left = s[:i]
                    right = s[i:]
                    if (left in self.dict_ and self.dict_[left]) or isPalindrome(left):
                        self.dict_[left] = True
                        possible = backtracking(right)
                        for line in possible:
                            ret.append([left]+line)
                return ret
        return backtracking(s)
S = Solution()
print S.partition('abab')




