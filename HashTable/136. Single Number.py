###########################################
# Author: Tinkle
# E-mail: shutingnupt@gmail.com
# Name:  Single Number.py
# Creation Time: 2018/1/22
###########################################
'''
Given an array of integers, every element appears twice except for one. Find that single one.

Note:
Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?


'''
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ret=0
        for i in nums:
            ret=ret^i
        return ret