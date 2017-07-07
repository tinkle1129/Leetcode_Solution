# - * - coding:utf8 - * - -
###########################################
# Author: Tinkle
# E-mail: shutingnupt@gmail.com
# Name:  Plus One.py
# Creation Time: 2017/7/7
###########################################
'''
Given a non-negative integer represented as a non-empty array of digits, plus one to the integer.

You may assume the integer do not contain any leading zero, except the number 0 itself.

The digits are stored such that the most significant digit is at the head of the list.
'''
class Solution(object):
    def plusOne(self, digits):
        digits.reverse()
        flag=1
        for i in range(len(digits)):
            if digits[i]+flag<10:
                digits[i]+=flag
                flag=0
            else:
                digits[i]=0
                flag=1
        if flag==1:
            digits.append(1)
        digits.reverse()
        return digits