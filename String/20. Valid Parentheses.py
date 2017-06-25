###########################################
# Author: Tinkle
# E-mail: shutingnupt@gmail.com
# Name:  Valid Parentheses.py
# Creation Time: 2017/6/25
###########################################
'''
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

The brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]" and "([)]" are not.


'''


class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        dic = {')':'(',']':'[','}':'{'}
        for i in s:
            if i in ['(','[','{']:
                stack.append(i)
            elif i in [')',']','}']:
                if len(stack) and stack[-1]==dic[i]:
                    stack.pop()
                else:
                    return False
            else:
                return False
        if len(stack)==0:
            return True
        return False

S = Solution()
print S.isValid('()')
print S.isValid('([)]')
print S.isValid("()[]{}")