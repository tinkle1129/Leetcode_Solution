# - * - coding:utf8 - * - -
###########################################
# Author: Tinkle
# E-mail: shutingnjupt@gmail.com
# Name:  Power of Four.py
# Creation Time: 2017/9/5
###########################################
'''
Given an integer (signed 32 bits), write a function to check whether it is a power of 4.

Example:
Given num = 16, return true. Given num = 5, return false.

Follow up: Could you solve it without loops/recursion?

Credits:
Special thanks to @yukuairoy for adding this problem and creating all test cases.


'''
class Solution(object):
    def isPowerOfFour(self,num):
        '''
        :param num: int
        :return: bool
        '''
        return num>0 and num&(num-1) ==0 and num&0x55555555 == num