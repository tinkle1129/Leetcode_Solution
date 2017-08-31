# - * - coding:utf8 - * - -
###########################################
# Author: Tinkle
# E-mail: shutingnjupt@gmail.com
# Name:   Burst Balloons.py
# Creation Time: 2017/8/31
###########################################
'''
Given n balloons, indexed from 0 to n-1. Each balloon is painted with a number on it represented by array nums. You are asked to burst all the balloons. If the you burst balloon i you will get nums[left] * nums[i] * nums[right] coins. Here left and right are adjacent indices of i. After the burst, the left and right then becomes adjacent.

Find the maximum coins you can collect by bursting the balloons wisely.

Note:
(1) You may imagine nums[-1] = nums[n] = 1. They are not real therefore you can not burst them.
(2) 0 ≤ n ≤ 500, 0 ≤ nums[i] ≤ 100

Example:

Given [3, 1, 5, 8]

Return 167

    nums = [3,1,5,8] --> [3,5,8] -->   [3,8]   -->  [8]  --> []
   coins =  3*1*5      +  3*5*8    +  1*3*8      + 1*8*1   = 167
'''


class Solution(object):
    def boom(self,nums,res,left,right):
        if right-left<=1:
            return 0
        if res[left][right]>0:
            return res[left][right]
        maxx = 0
        for i in range(left+1,right):
            maxx = max(maxx,nums[i]*nums[left]*nums[right]+self.boom(nums,res,left,i)+
                       self.boom(nums,res,i,right))
        res[left][right]=maxx
        return res[left][right]

    def maxCoins(self,nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = [1] + nums + [1]
        n  = len(nums)
        res = [[0]*n for x in range(n)]
        return self.boom(nums,res,0,len(nums)-1)

    def maxCoins_(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        visited = []
        visited_value = []
        def coins(nums):
            if len(nums) == 0:
                return 0
            ret = 0
            for i in range(len(nums)):
                score = nums[i]
                if i>0:
                    score *= nums[i-1]
                if i<len(nums)-1:
                    score *= nums[i+1]
                newnums = nums[:i]+nums[i+1:]
                if newnums in visited:
                    idx = visited.index(newnums)
                    ret = max(ret,visited_value[idx]+score)
                else:
                    visited_value.append(coins(newnums))
                    visited.append(newnums)
                    ret = max(ret, visited_value[-1] + score)
            visited.append(nums)
            visited_value.append(ret)
            return ret
        return coins(nums)


S = Solution()
print S.maxCoins([3,1,5,8])
print S.maxCoins([35,16,83,87,84,59,48,41,20,54])
print S.maxCoins([7,9,8,0,7,1,3,5,5,2,3,3,3])