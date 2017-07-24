# - * - coding:utf8 - * - -
###########################################
# Author: Tinkle
# E-mail: shutingnjupt@gmail.com
# Name: Palindrome Partitioning II.py
# Creation Time: 2017/7/24
###########################################
'''
Given a string s, partition s such that every substring of the partition is a palindrome.

Return the minimum cuts needed for a palindrome partitioning of s.

For example, given s = "aab",
Return 1 since the palindrome partitioning ["aa","b"] could be produced using 1 cut.
'''


class Solution(object):
    def minCut(self, s):
        """
        :type s: str
        :rtype: int
        """
        def isPalindrome(string):
            if len(string)==1:
                return True
            start = 0
            end = len(string)-1
            while(start<=end):
                if string[start]!=string[end]:
                    return False
                start +=1
                end -=1
            return True
        self.dict_ = {}

        def backtracking(s):
            print s
            if (s in self.dict_ and self.dict_[s]) or isPalindrome(s):
                self.dict_[s] = True
                return 0

            self.dict_[s] = False

            ret = len(s)-1
            for i in range(1,len(s)):
                left = s[i:]
                right = s[:i]
                if (left in self.dict_ and self.dict_[left]) or isPalindrome(left):
                    self.dict_[left] = True

                    mincut = backtracking(right)
                    ret = min(ret,1+mincut)
                else:
                    self.dict_[left] = False
            return ret
        return backtracking(s)
S = Solution()
#print S.minCut('cdd')
#print S.minCut('ababc')
#print S.minCut('aab')
print S.minCut("fifgbeajcacehiicccfecbfhhgfiiecdcjjffbghdidbhbdbfbfjccgbbdcjheccfbhafehieabbdfeigbiaggchaeghaijfbjhi")