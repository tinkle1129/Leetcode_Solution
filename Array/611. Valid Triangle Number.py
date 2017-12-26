# - * - coding:utf8 - * - -
###########################################
# Author: Tinkle
# E-mail: shutingnjupt@gmail.com
# Name: Valid Triangle Number.py
# Creation Time: 2017/12/26
###########################################
'''
Given an array consists of non-negative integers, your task is to count the number of triplets chosen from the array that can make triangles if we take them as side lengths of a triangle.
Example 1:
Input: [2,2,3,4]
Output: 3
Explanation:
Valid combinations are:
2,3,4 (using the first 2)
2,3,4 (using the second 2)
2,2,3
Note:
The length of the given array won't exceed 1000.
The integers in the given array are in the range of [0, 1000].
'''
class Solution(object):
    def triangleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        size = len(nums)
        ret = 0
        for i in range(size-2):
            if nums[i]==0:
                continue
            k = i+2
            for j in range(i+1,size-1):
                while(k<size and nums[k]<nums[i]+nums[j]):
                    k+=1
                ret+=k-j-1
        return ret