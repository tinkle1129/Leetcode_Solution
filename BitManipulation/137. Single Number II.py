# - * - coding:utf8 - * - -
###########################################
# Author: Tinkle
# E-mail: shutingnjupt@gmail.com
# Name:  Single Number II.py
# Creation Time: 2018/3/5
###########################################
'''
Given an array of integers, every element appears three times except for one, which appears exactly once. Find that single one.

Note:
Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?
'''
class Solution(object):
    def singleNumber1(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        flag1=0;flag2=0
        for i in nums:
            flag2 ^=(flag1 & i)
            flag1 ^= i
            flag3 =(flag2 & flag1)
            flag1 ^=flag3
            flag2 ^=flag3
        return flag1


class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        bitArrays = [0]*33
        for num in nums:
            i,flag = 0,1
            if num<0:
                num = -num
                bitArrays[32]+=1
            while(i<32):
                if num & flag: bitArrays[i]+=1
                flag = flag<<1
                i+=1
        i, ret,flag = 0,0, 1
        while(i<32):
            if bitArrays[i]%3: ret+=flag
            flag=flag<<1
            i+=1
        if bitArrays[32]%3: ret = -ret
        return ret


