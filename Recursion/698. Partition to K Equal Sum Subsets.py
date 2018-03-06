# - * - coding:utf8 - * - -
###########################################
# Author: Tinkle
# E-mail: shutingnjupt@gmail.com
# Name: Partition to K Equal Sum Subsets.py
# Creation Time: 2018/3/6
###########################################
'''
Given an array of integers nums and a positive integer k, find whether it's possible to divide this array into k non-empty subsets whose sums are all equal.
Example 1:
Input: nums = [4, 3, 2, 3, 5, 2, 1], k = 4
Output: True
Explanation: It's possible to divide it into 4 subsets (5), (1, 4), (2,3), (2,3) with equal sums.
Note:
1 <= k <= len(nums) <= 16.
0 < nums[i] < 10000.
'''


class Solution(object):
    def canPartitionKSubsets(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        if sum(nums) % k: return False
        dmaps = {}
        def dfs(nums, target, k):
            if nums == []: return False
            if k == 1: return sum(nums) == target
            key = (tuple(nums), k)
            if key in dmaps: return dmaps[key]
            size = len(nums)
            ans = False
            for x in range(1 << size):
                tsums = 0
                rest = []
                for y in range(size):
                    if (x >> y) & 1:
                        tsums += nums[y]
                    else:
                        rest.append(nums[y])
                if tsums == target and dfs(rest, target, k - 1):
                    ans = True
                    break
            dmaps[key] = ans
            return dmaps[key]
        return dfs(sorted(nums), sum(nums) / k, k)

