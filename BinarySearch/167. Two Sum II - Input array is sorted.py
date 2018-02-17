###########################################
# Author: Tinkle
# E-mail: shutingnupt@gmail.com
# Name:  Two Sum II - Input array is sorted.py
# Creation Time: 2018/1/22
###########################################
'''
Given an array of integers that is already sorted in ascending order, find two numbers such that they add up to a specific target number.

The function twoSum should return indices of the two numbers such that they add up to the target, where index1 must be less than index2. Please note that your returned answers (both index1 and index2) are not zero-based.

You may assume that each input would have exactly one solution and you may not use the same element twice.

Input: numbers={2, 7, 11, 15}, target=9
Output: index1=1, index2=2
'''
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)):
            tmp=target-nums[i]
            start=i+1
            end=len(nums)-1
            while(start<=end):
                if tmp==nums[end]:
                    return [i+1,end+1]
                if tmp==nums[start]:
                    return [i+1,start+1]
                mid = (end - start) / 2+start
                if mid==start or mid==end:
                    break
                if tmp > nums[mid]:
                    start=mid
                elif tmp< nums[mid]:
                    end=mid
                else:
                    return [i+1,mid+1]