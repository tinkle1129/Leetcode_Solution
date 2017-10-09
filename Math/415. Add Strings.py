# - * - coding:utf8 - * - -
###########################################
# Author: Tinkle
# E-mail: shutingnjupt@gmail.com
# Name:  Add Strings.py
# Creation Time: 2017/10/9
###########################################
'''
Given two non-negative integers num1 and num2 represented as string, return the sum of num1 and num2.

Note:

The length of both num1 and num2 is < 5100.
Both num1 and num2 contains only digits 0-9.
Both num1 and num2 does not contain any leading zero.
You must not use any built-in BigInteger library or convert the inputs to integer directly.
'''


class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        len1 = len(num1)
        len2 = len(num2)
        length = max(len1, len2)
        if len1 < len2:
            num1 = '0' * (len2 - len1) + num1
        else:
            num2 = '0' * (len1 - len2) + num2
        ret = ''
        flag = 0
        for i in range(length):
            idx = length - 1 - i
            num = int(num1[idx]) + int(num2[idx]) + flag
            ret = str(num % 10) + ret
            flag = num / 10
        if flag:
            ret = '1' + ret
        return ret

