# - * - coding:utf8 - * - -
###########################################
# Author: Tinkle
# E-mail: shutingnupt@gmail.com
# Name:   Target Sum.py
# Creation Time: 2018/3/17
###########################################
'''
You are given a list of non-negative integers, a1, a2, ..., an, and a target, S. Now you have 2 symbols + and -. For each integer, you should choose one from + and - as its new symbol.

Find out how many ways to assign symbols to make sum of integers equal to target S.

Example 1:
Input: nums is [1, 1, 1, 1, 1], S is 3.
Output: 5
Explanation:

-1+1+1+1+1 = 3
+1-1+1+1+1 = 3
+1+1-1+1+1 = 3
+1+1+1-1+1 = 3
+1+1+1+1-1 = 3

There are 5 ways to assign symbols to make the sum of nums be target 3.
Note:
The length of the given array is positive and will not exceed 20.
The sum of elements in the given array will not exceed 1000.
Your output answer is guaranteed to be fitted in a 32-bit integer.

'''


class Solution(object):
    def findTargetSumWays(self, nums, S):
        if nums == []: return 0
        dics = {nums[0]: 1, -nums[0]: 1} if nums[0] else {0: 2}
        for i in range(1, len(nums)):
            tmp = {}
            for d in dics:
                tmp[d + nums[i]] = tmp.get(d + nums[i], 0) + dics.get(d, 0)
                tmp[d - nums[i]] = tmp.get(d - nums[i], 0) + dics.get(d, 0)
            dics = tmp
        return dics.get(S, 0)
