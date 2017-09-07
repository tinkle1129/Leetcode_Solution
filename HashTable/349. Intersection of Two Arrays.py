# - * - coding:utf8 - * - -
###########################################
# Author: Tinkle
# E-mail: shutingnjupt@gmail.com
# Name: Intersection of Two Arrays.py
# Creation Time: 2017/9/7
###########################################
'''
Given two arrays, write a function to compute their intersection.

Example:
Given nums1 = [1, 2, 2, 1], nums2 = [2, 2], return [2].
'''
class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        dic = {};ans = []
        for num in nums1:
            dic[num] = 0
        for num in nums2:
            if num in dic:
                ans.append(num)
                dic.pop(num)
        return ans

