# - * - coding:utf8 - * - -
###########################################
# Author: Tinkle
# E-mail: shutingnjupt@gmail.com
# Name:   Minimum Moves to Equal Array Elements II.py
# Creation Time: 2018/3/23
###########################################
'''
Given a non-empty integer array, find the minimum number of moves required to make all array elements equal, where a move is incrementing a selected element by 1 or decrementing a selected element by 1.

You may assume the array's length is at most 10,000.

Example:

Input:
[1,2,3]

Output:
2

Explanation:
Only two moves are needed (remember each move increments or decrements one element):

[1,2,3]  =>  [2,2,3]  =>  [2,2,2]
'''
import sys
class Solution(object):
    def minMoves2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        size = len(nums)
        sums = sum(nums)
        lastValue = 0
        ans = sys.maxint
        for i,num in enumerate(nums):
            right = sums-lastValue-num-(size-1-i)*num
            left = i*num-lastValue
            print left+right
            ans = min(ans,left+right)
            lastValue+=num
        return ans
S = Solution()
