# - * - coding:utf8 - * - -
###########################################
# Author: Tinkle
# E-mail: shutingnjupt@gmail.com
# Name:  Single Number III.py
# Creation Time: 2018/3/5
###########################################
'''
Given an array of numbers nums, in which exactly two elements appear only once and all the other elements appear exactly twice. Find the two elements that appear only once.

For example:

Given nums = [1, 2, 1, 3, 2, 5], return [3, 5].

Note:
The order of the result is not important. So in the above example, [5, 3] is also correct.
Your algorithm should run in linear runtime complexity. Could you implement it using only constant space complexity?
'''
class Solution1:
    # 返回[a,b] 其中ab是出现一次的两个数字
    def FindNumsAppearOnce(self, array):
        # write code here
        ans,a1,a2,flag= 0,0,0,1
        for num in array:
            ans = ans ^ num
        while(ans):
            if ans%2 == 0:
                ans = ans >>1
                flag = flag <<1
            else:
                break
        for num in array:
            if num & flag:
                a1 = a1 ^ num
            else:
                a2 = a2 ^ num
        return a1,a2
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        result=0
        for i in nums:
            result=result^i
        flag=result&(~(result-1))
        ans=[0,0]
        for i in nums:
            if i&flag:
                ans[1]=ans[1]^i
            else:
                ans[0]=ans[0]^i
        return ans
