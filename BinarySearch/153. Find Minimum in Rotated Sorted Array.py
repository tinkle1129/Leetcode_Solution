# - * - coding:utf8 - * - -
###########################################
# Author: Tinkle
# E-mail: shutingnjupt@gmail.com
# Name: Find Minimum in Rotated Sorted Array.py
# Creation Time: 2017/7/30
###########################################
'''
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

Find the minimum element.

You may assume no duplicate exists in the array.

'''


class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        start = 0;
        end = len(nums) - 1
        while (start < end):
            mid = start + (end - start) / 2
            if mid != len(nums) - 1 and nums[mid] > nums[mid + 1]:
                return nums[mid + 1]
            elif nums[mid] < nums[start]:
                end = mid
            elif nums[mid] > nums[end]:
                start = mid
            else:
                return nums[start]
        return nums[start]
