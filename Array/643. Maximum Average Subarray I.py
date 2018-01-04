# - * - coding:utf8 - * - -
###########################################
# Author: Tinkle
# E-mail: shutingnjupt@gmail.com
# Name:  Maximum Average Subarray I。py
# Creation Time: 2018/1/4
###########################################
'''
Given an array consisting of n integers, find the contiguous subarray of given length k that has the maximum average value. And you need to output the maximum average value.

Example 1:
Input: [1,12,-5,-6,50,3], k = 4
Output: 12.75
Explanation: Maximum average is (12-5-6+50)/4 = 51/4 = 12.75
Note:
1 <= k <= n <= 30,000.
Elements of the given array will be in the range [-10,000, 10,000].
'''

class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        size = len(nums)
        sum_ = sum(nums[0:k])
        tmp = sum_
        for i in range(k,size):
            tmp = tmp+nums[i]-nums[i-k]
            sum_ = max(tmp,sum_)
        return sum_*1.0/k