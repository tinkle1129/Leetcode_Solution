# - * - coding:utf8 - * - -
###########################################
# Author: Tinkle
# E-mail: shutingnjupt@gmail.com
# Name: Remove Duplicates from Sorted Array.py
# Creation Time: 2017/1/21
###########################################
'''
Given a sorted array, remove the duplicates in-place such that each element appear only once and return the new length.

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

Example:

Given nums = [1,1,2],

Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively.
It doesn't matter what you leave beyond the new length.

'''
class Solution(object):
    def removeDuplicates(self, nums):
        if nums == []: return 0
        j = 1
        for i in range(1,len(nums)):
            if nums[i]!=nums[i-1]:
                nums[j] = nums[i]
                j+=1
        return j