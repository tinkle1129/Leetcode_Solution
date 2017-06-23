###########################################
# Author: Tinkle
# E-mail: shutingnupt@gmail.com
# Name: Median of Two Sorted Arrays.py
# Creation Time: 2017/6/20
###########################################
'''
There are two sorted arrays nums1 and nums2 of size m and n respectively.

Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

Example 1:
nums1 = [1, 3]
nums2 = [2]

The median is 2.0
Example 2:
nums1 = [1, 2]
nums2 = [3, 4]

The median is (2 + 3)/2 = 2.5
'''
class Solution(object):
    def findDigit(self,nums1,nums2,idx):
        if len(nums1)>len(nums2):
            return self.findDigit(nums2,nums1,idx)
        if len(nums1) == 0:
            return nums2[idx-1]
        if idx == 1:
            return min(nums1[0],nums2[0])
        l1_mid = min(idx/2,len(nums1))
        l2_mid = idx-l1_mid
        if nums1[l1_mid-1] <= nums2[l2_mid-1]:
            return self.findDigit(nums1[l1_mid:],nums2,l2_mid)
        else:
            return self.findDigit(nums1,nums2[l2_mid:],l1_mid)

    def findMedianSortedArrays(self,nums1,nums2):
        '''
        :param nums1: List[int]
        :param nums2: List[int]
        :return: float
        '''
        total_length = len(nums1) + len(nums2)
        if total_length%2 == 1:
            return self.findDigit(nums1,nums2,total_length/2+1)
        else:
            return (self.findDigit(nums1,nums2,total_length/2)+self.findDigit(nums1,nums2,total_length/2+1))*0.5

nums1 = [1,3]#,3,4]
nums2 = [2]#4,6,9,10,23,30,31,32,33]
S = Solution()
print S.findMedianSortedArrays(nums1,nums2)