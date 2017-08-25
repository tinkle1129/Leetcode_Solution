# - * - coding:utf8 - * - -
###########################################
# Author: Tinkle
# E-mail: shutingnupt@gmail.com
# Name:  Maximum Subarray.py
# Creation Time: 2017/7/5
###########################################
'''
Find the contiguous subarray within an array (containing at least one number)
which has the largest sum.
For example, given the array [-2,1,-3,4,-1,2,1,-5,4],
the contiguous subarray [4,-1,2,1] has the largest sum = 6.
'''
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums == []:
            return 0
        dp = nums[0]
        ret = nums[0]
        for i in range(1,len(nums)):
            dp = max(dp+nums[i],nums[i])
            ret = max(ret,dp)
        return ret

S = Solution()
print S.maxSubArray([-2,1,-3,4,-1,2,1,-5,4])