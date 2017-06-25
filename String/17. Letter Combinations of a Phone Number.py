###########################################
# Author: Tinkle
# E-mail: shutingnupt@gmail.com
# Name:  Letter Combinations of a Phone Number.py
# Creation Time: 2017/6/24
###########################################
'''
Input:Digit string "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
'''
class Solution(object):
    def __init__(self):
        self.ret = []
        self.dic = {'2':['a','b','c'],
               '3':['d','e','f'],
               '4':['g','h','i'],
               '5':['j','k','l'],
               '6':['m','n','o'],
               '7':['p','q','r','s'],
               '8':['t','u','v'],
               '9':['w','x','y','z']}
    def depthsearch(self,digit,curstr=''):
        if len(digit)>=1:
            if len(digit)==1:
                for idx in self.dic[digit[0]]:
                    self.ret.append(curstr+idx)
            else:
                for idx in self.dic[digit[0]]:
                    self.depthsearch(digit[1:],curstr+idx)

    def letterCombinations(self, digit):
        '''
        :param digit: str
        :return: list[str]
        '''
        self.depthsearch(digit)
        return self.ret

S = Solution()
print S.letterCombinations('')