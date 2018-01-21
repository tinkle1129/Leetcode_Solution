###########################################
# Author: Tinkle
# E-mail: shutingnupt@gmail.com
# Name:  Merge Sorted Array.py
# Creation Time: 2018/1/21
###########################################
'''
Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.

Note:
You may assume that nums1 has enough space (size that is greater or equal to m + n) to hold additional elements from nums2.
The number of elements initialized in nums1 and nums2 are m and n respectively.
'''
class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        l=m+n-1
        i=min(len(nums1)-1,m-1)
        j=min(len(nums2)-1,n-1)
        while(i>=0 and j>=0):
            if(nums1[i]>nums2[j]):
                nums1[l]=nums1[i]
                l=l-1;i=i-1
            else:
                nums1[l]=nums2[j]
                l=l-1;j=j-1
        while(i>=0):
            nums1[l]=nums1[i]
            l=l-1
            i=i-1
        while(j>=0):
            nums1[l]=nums2[j]
            l=l-1
            j=j-1