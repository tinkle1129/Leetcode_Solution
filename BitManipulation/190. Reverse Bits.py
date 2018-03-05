# - * - coding:utf8 - * - -
###########################################
# Author: Tinkle
# E-mail: shutingnjupt@gmail.com
# Name:  Reverse Bits.py
# Creation Time: 2018/3/5
###########################################
'''
Reverse bits of a given 32 bits unsigned integer.

For example, given input 43261596 (represented in binary as 00000010100101000001111010011100), return 964176192 (represented in binary as 00111001011110000010100101000000).

Follow up:
If this function is called many times, how would you optimize it?

Related problem: Reverse Integer

Credits:
Special thanks to @ts for adding this problem and creating all test cases.
'''
class Solution(object):
    def reverseBits(self, n):
        """
        :type n: int
        :rtype: int
        """
        ret=0
        flag=0
        while(flag<32):
            ret=(ret<<1)+(n&1)
            n=n>>1
            flag=flag+1
        return ret