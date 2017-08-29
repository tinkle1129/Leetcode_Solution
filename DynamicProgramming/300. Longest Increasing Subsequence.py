# - * - coding:utf8 - * - -
###########################################
# Author: Tinkle
# E-mail: shutingnjupt@gmail.com
# Name:  Longest Increasing Subsequence.py
# Creation Time: 2017/8/29
###########################################
'''
Given an unsorted array of integers, find the length of longest increasing subsequence.

For example,
Given [10, 9, 2, 5, 3, 7, 101, 18],
The longest increasing subsequence is [2, 3, 7, 101], therefore the length is 4. Note that there may be more than one LIS combination, it is only necessary for you to return the length.

Your algorithm should run in O(n2) complexity.

Follow up: Could you improve it to O(n log n) time complexity?
'''


class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)==0:
            return 0
        ret = 0
        dp = [0 for i in range(len(nums))]
        for i in range(len(nums)):
            for j in range(i):
                if nums[i]>nums[j]:
                    dp[i] = max(dp[j],dp[i])
            dp[i]+=1
            ret = max(ret,dp[i])
        return ret

S = Solution()
print S.lengthOfLIS([10, 9, 2, 5, 3, 100,7, 101, 18])
print S.lengthOfLIS([10,8,4,5,6,7,8,9,2,3,10,11,12,14])