# - * - coding:utf8 - * - -
###########################################
# Author: Tinkle
# E-mail: shutingnupt@gmail.com
# Name: Sort Colors.py
# Creation Time: 2017/7/10
###########################################
'''
ven an array with n objects colored red, white or blue, sort them so that objects of the same color are adjacent, with the colors in the order red, white and blue.

Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.

Note:
You are not suppose to use the library's sort function for this problem.
'''


class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if len(nums) == 0:
            return
        low = 0;
        mid = 0;
        high = len(nums) - 1
        while (mid <= high):
            if nums[mid] == 0:
                tmp = nums[low]
                nums[low] = nums[mid]
                nums[mid] = tmp
                low += 1
                mid += 1
            elif nums[mid] == 1:
                mid += 1
            else:
                tmp = nums[high]
                nums[high] = nums[mid]
                nums[mid] = tmp
                high -= 1

