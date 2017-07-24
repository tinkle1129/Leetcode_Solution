# - * - coding:utf8 - * - -
###########################################
# Author: Tinkle
# E-mail: shutingnjupt@gmail.com
# Name: Longest Consecutive Sequence.py
# Creation Time: 2017/7/22
###########################################
'''
Given an unsorted array of integers, find the length of the longest consecutive elements sequence.

For example,
Given [100, 4, 200, 1, 3, 2],
The longest consecutive elements sequence is [1, 2, 3, 4]. Return its length: 4.

Your algorithm should run in O(n) complexity.
'''


class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        Map = {}
        for num in nums:
            Map[num] = True
        ret = 0
        for k,v in Map.items():
            if not v:
                continue
            left = k-1
            right = k+1
            while(left in Map and Map[left]):
                Map[left] = False
                left = left-1
            while(right in Map and Map[right]):
                Map[right] = False
                right = right+1
            ret = max(ret,right-left-1)
        return ret
