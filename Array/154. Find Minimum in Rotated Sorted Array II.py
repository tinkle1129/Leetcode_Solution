# - * - coding:utf8 - * - -
###########################################
# Author: Tinkle
# E-mail: shutingnjupt@gmail.com
# Name: Find Minimum in Rotated Sorted Array II.py
# Creation Time: 2017/7/30
###########################################
'''
Follow up for "Find Minimum in Rotated Sorted Array":
What if duplicates are allowed?

Would this affect the run-time complexity? How and why?
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

Find the minimum element.
'''


class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        start = 0; end = len(nums)-1
        while(start<end):
            while(start<end and nums[end] == nums[start]):
                start +=1
            while(start<end and nums[start] == nums[start+1]):
                start +=1
            while(start<end and nums[end] == nums[end-1]):
                end -=1
            if start == end:
                break
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

S = Solution()
print S.findMin([2,3,-1,0,0,0,0,0,0,1,2])