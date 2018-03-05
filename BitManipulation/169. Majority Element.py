# - * - coding:utf8 - * - -
###########################################
# Author: Tinkle
# E-mail: shutingnjupt@gmail.com
# Name:  Majority Element.py
# Creation Time: 2018/3/5
###########################################
'''
Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.

You may assume that the array is non-empty and the majority element always exist in the array.

Credits:
Special thanks to @ts for adding this problem and creating all test cases.

Seen this question in a real interview before?

'''
class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def majorityElement(self, nums):
        bit = [0] * 32
        for num in nums:
            for j in xrange(32):
                bit[j] += num >> j & 1
        res = 0
        for i, val in enumerate(bit):
            if val > len(nums) // 2:
                if i == 31:
                    res = -((1 << 31) - res)
                else:
                    res |= 1 << i
        return res