# - * - coding:utf8 - * - -
###########################################
# Author: Tinkle
# E-mail: shutingnjupt@gmail.com
# Name:  Longest Harmonious Subsequence.py
# Creation Time: 2018/1/8
###########################################
'''
We define a harmonious array is an array where the difference between its maximum value and its minimum value is exactly 1.

Now, given an integer array, you need to find the length of its longest harmonious subsequence among all its possible subsequences.

Example 1:
Input: [1,3,2,2,5,2,3,7]
Output: 5
Explanation: The longest harmonious subsequence is [3,2,2,2,3].
Note: The length of the input array will not exceed 20,000.
'''
import collections
class Solution(object):
    def findLHS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        hashtable = collections.defaultdict(int)
        for num in nums:
            hashtable[num]+=1
        lhs = 0
        for num in hashtable.keys():
            if num-1 in hashtable:
                lhs = max(lhs,hashtable[num]+hashtable[num-1])
            if num+1 in hashtable:
                lhs = max(lhs,hashtable[num]+hashtable[num+1])
        return lhs
