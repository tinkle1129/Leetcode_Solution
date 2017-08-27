# - * - coding:utf8 - * - -
###########################################
# Author: Tinkle
# E-mail: shutingnjupt@gmail.com
# Name:  Move Zeroes.py
# Creation Time: 2017/8/27
###########################################
'''
Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

For example, given nums = [0, 1, 0, 3, 12], after calling your function, nums should be [1, 3, 12, 0, 0].

Note:
You must do this in-place without making a copy of the array.
Minimize the total number of operations.
'''
class Solution(object):
    def moveZeroes(self, nums):
        '''
        :param nums: list[int]
        :return: None
        '''
        idx = 0
        for i in range(len(nums)):
            if nums[i]!=0:
                nums[idx] = nums[i]
                idx +=1
        for i in range(idx,len(nums)):
            nums[i] = 0

S = Solution()
nums = [0,1,0,3,12]
S.moveZeroes(nums)
print nums