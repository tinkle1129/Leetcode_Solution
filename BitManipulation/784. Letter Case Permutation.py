# - * - coding:utf8 - * - -
###########################################
# Author: Tinkle
# E-mail: shutingnjupt@gmail.com
# Name: Letter Case Permutation.py
# Creation Time: 2018/3/5
###########################################
'''
Given a string S, we can transform every letter individually to be lowercase or uppercase to create another string.  Return a list of all possible strings we could create.

Examples:
Input: S = "a1b2"
Output: ["a1b2", "a1B2", "A1b2", "A1B2"]

Input: S = "3z4"
Output: ["3z4", "3Z4"]

Input: S = "12345"
Output: ["12345"]
Note:

S will be a string with length at most 12.
S will consist only of letters or digits.

'''
class Solution(object):
    def letterCasePermutation(self, S):
        """
        :type S: str
        :rtype: List[str]
        """
        cnt,ret = 0,[]
        for token in S:
            if token.isalpha(): cnt+=1
        for i in range(2**cnt):
            state = list('{:b}'.format(i))
            state = ['0'] * (cnt - len(state)) + state
            idx,tmp = 0,''
            for token in S:
                if token.isalpha():
                    if state[idx]=='0':
                        tmp+=token.lower()
                    else:
                        tmp+=token.upper()
                    idx+=1
                else:
                    tmp+=token
            ret.append(tmp)
        return ret


S = Solution()
print S.letterCasePermutation('1234dd')