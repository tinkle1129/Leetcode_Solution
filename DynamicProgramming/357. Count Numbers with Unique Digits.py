# - * - coding:utf8 - * - -
###########################################
# Author: Tinkle
# E-mail: shutingnjupt@gmail.com
# Name: Count Numbers with Unique Digits.py
# Creation Time: 2017/9/8
###########################################
'''
Given a non-negative integer n, count all numbers with unique digits, x, where 0 ≤ x < 10n.

Example:
Given n = 2, return 91. (The answer should be the total numbers in the range of 0 ≤ x < 100, excluding [11,22,33,44,55,66,77,88,99])
'''
class Solution(object):
    def countNumbersWithUniqueDigits(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp=[1]
        for i in range(1,n+1):
            if i==1:
                dp.append(10)
            else:
                tmp=9
                flag=9
                j=i-1
                while(j>0):
                    tmp=tmp*flag
                    flag=flag-1
                    j=j-1
                dp.append(dp[-1]+tmp)
        return dp[-1]

