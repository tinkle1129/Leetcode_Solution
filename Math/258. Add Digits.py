# - * - coding:utf8 - * - -
###########################################
# Author: Tinkle
# E-mail: shutingnjupt@gmail.com
# Name:   Add Digits.py
# Creation Time: 2018/3/22
###########################################
'''
Given a non-negative integer num, repeatedly add all its digits until the result has only one digit.

For example:

Given num = 38, the process is like: 3 + 8 = 11, 1 + 1 = 2. Since 2 has only one digit, return it.

Follow up:
Could you do it without any loop/recursion in O(1) runtime?

Credits:
Special thanks to @jianchao.li.fighter for adding this problem and creating all test cases.
'''
class Solution(object):
    # loop/recursion
    def addDigits1(self, num):
        """
        :type num: int
        :rtype: int
        """
        num = str(num)
        while(len(num)>1):
            ans = 0
            for i in num:
                ans +=int(i)
            num = str(ans)
        return int(num)

    # O(1)time
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """

        num = str(num)
        ans = 0
        for n in num:
            ans+=int(n)
            if ans>=10:
                ans=(ans%10)+(ans/10)
        return ans