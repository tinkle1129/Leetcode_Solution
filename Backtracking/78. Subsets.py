# - * - coding:utf8 - * - -
###########################################
# Author: Tinkle
# E-mail: shutingnupt@gmail.com
# Name: Subsets.py
# Creation Time: 2017/7/11
###########################################
'''
Given a set of distinct integers, nums, return all possible subsets.

Note: The solution set must not contain duplicate subsets.

For example,
If nums = [1,2,3], a solution is:

[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]

'''
class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ret=[]
        if not len(nums):
            return ret
        for i in range(2**(len(nums))):
            tmp=[]
            state=list('{:b}'.format(i))
            state=['0']*(len(nums)-len(state))+state
            for j in range(len(state)):
                if state[j]=='1':
                    tmp.append(nums[j])
            ret.append(tmp)
        return ret