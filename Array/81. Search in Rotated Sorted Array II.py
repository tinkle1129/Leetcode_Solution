# - * - coding:utf8 - * - -
###########################################
# Author: Tinkle
# E-mail: shutingnupt@gmail.com
# Name: Search in Rotated Sorted Array II.py
# Creation Time: 2017/7/11
###########################################
'''
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

Write a function to determine if a given target is in the array.

The array may contain duplicates.
'''

class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        if len(nums):
            start = 0
            end = len(nums)-1

            while(start<end):
                mid = (start+end)/2
                while(start<=mid and nums[start]==nums[mid]):
                    start+=1
                while(end>=mid and nums[end]==nums[mid]):
                    end -=1

                if nums[mid]==target or nums[start]==target or nums[end] == target:
                    return True
                if (nums[start]<target) and  (nums[mid]>target or nums[start]>nums[mid]):
                    end = mid
                    start +=1
                elif nums[start]>target and nums[mid]>target and nums[mid]<nums[end]:
                    end = mid
                    start +=1
                else:
                    start = mid
                    end -=1
            if start<len(nums) and end>=0 and (nums[start]==target or nums[end] == target):
                return True
            else:
                return False

        else:
            return False
S =Solution()
print S.search([15,16,19,20,25,1,3,4,5,7,10,14],
25)
print S.search([10,10,10,-10,-10,-10,-10,-9,-9,-9,-9,-9,-9,-9,-8,-8,-8,-8,-8,-8,-8,-8,-7,-7,-7,-7,-6,-6,-6,-5,-5,-5,-4,-4,-4,-4,-3,-3,-2,-2,-2,-2,-2,-2,-2,-2,-1,-1,-1,-1,-1,0,0,0,0,0,0,0,1,1,1,1,2,2,2,2,2,2,2,3,3,3,4,4,4,5,5,5,5,6,6,6,7,7,7,7,7,8,8,8,8,9,9,9,9,9,9,9,10,10]
,-6)
print S.search([4,5,6,7,0,1,2],0)

