###########################################
# Author: Tinkle
# E-mail: shutingnupt@gmail.com
# Name:  Majority Element.py
# Creation Time: 2018/1/23
###########################################
'''
Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.

You may assume that the array is non-empty and the majority element always exist in the array.

Credits:
Special thanks to @ts for adding this problem and creating all test cases.
'''


class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def majorityElement(self, nums):
        count = 0
        major_Element = 0
        for num in nums:
            if count == 0:
                major_Element = num
                count = count + 1
            else:
                if num == major_Element:
                    count = count + 1
                else:
                    count = count - 1
        return major_Element