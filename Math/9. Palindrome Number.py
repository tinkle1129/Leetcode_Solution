###########################################
# Author: Tinkle
# E-mail: shutingnupt@gmail.com
# Name:  Palindrome Number.py
# Creation Time: 2017/6/22
###########################################
class Solution(object):
    def isPalindrome(self,x):
        '''
        :param x: int
        :return: bool
        '''
        if x<0:
            return False
        tmp = x
        ret = 0
        while(x):
            ret = ret*10 + x%10
            x = x/10
        return ret == tmp

S = Solution()
S.isPalindrome(134321)