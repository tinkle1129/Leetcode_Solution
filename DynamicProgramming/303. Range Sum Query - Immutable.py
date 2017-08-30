# - * - coding:utf8 - * - -
###########################################
# Author: Tinkle
# E-mail: shutingnjupt@gmail.com
# Name:   Range Sum Query - Immutable.py
# Creation Time: 2017/8/30
###########################################
'''
Given an integer array nums, find the sum of the elements between indices i and j (i ≤ j), inclusive.

Example:
Given nums = [-2, 0, 3, -5, 2, -1]

sumRange(0, 2) -> 1
sumRange(2, 5) -> -1
sumRange(0, 5) -> -3
'''
class NumArray(object):
    def __init__(self, nums):
        self.Nums=[0]
        for i in range(len(nums)):
            self.Nums.append(self.Nums[i]+nums[i])
    def sumRange(self, i, j):
        return self.Nums[j+1]-self.Nums[i]