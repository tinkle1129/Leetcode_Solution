# - * - coding:utf8 - * - -
###########################################
# Author: Tinkle
# E-mail: shutingnjupt@gmail.com
# Name:  Binary Number with Alternating Bits.py
# Creation Time: 2018/3/5
###########################################
'''
Given a positive integer, check whether it has alternating bits: namely, if two adjacent bits will always have different values.
Example 1:
Input: 5
Output: True
Explanation:
The binary representation of 5 is: 101
Example 2:
Input: 7
Output: False
Explanation:
The binary representation of 7 is: 111.
Example 3:
Input: 11
Output: False
Explanation:
The binary representation of 11 is: 1011.
Example 4:
Input: 10
Output: True
Explanation:
The binary representation of 10 is: 1010.
'''
class Solution:
    def hasAlternatingBits(self, n):
        if not n:
            return False
        num = n ^ (n >> 1)
        return not (num & (num + 1))