# - * - coding:utf8 - * - -
###########################################
# Author: Tinkle
# E-mail: shutingnjupt@gmail.com
# Name:  Create Maximum Number.py
# Creation Time: 2017/9/2
###########################################
'''
Given two arrays of length m and n with digits 0-9 representing two numbers. Create the maximum number of length k <= m + n from digits of the two. The relative order of the digits from the same array must be preserved. Return an array of the k digits. You should try to optimize your time and space complexity.

Example 1:
nums1 = [3, 4, 6, 5]
nums2 = [9, 1, 2, 5, 8, 3]
k = 5
return [9, 8, 6, 5, 3]

Example 2:
nums1 = [6, 7]
nums2 = [6, 0, 4]
k = 5
return [6, 7, 6, 0, 4]

Example 3:
nums1 = [3, 9]
nums2 = [8, 9]
k = 3
return [9, 8, 9]
'''


class Solution(object):
    def maxNumber(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[int]
        """
        def getmaxarray(nums,t):
            stack = []
            size = len(nums)
            for idx in range(size):
                while stack and stack[-1]<nums[idx] and len(stack)+size-idx>t:
                    stack.pop()
                if len(stack)<t:
                    stack.append(nums[idx])
            return stack

        def merge(nums1,nums2):
            ans = []
            while nums1 or nums2:
                if nums1 > nums2:
                    ans.append(nums1[0])
                    nums1 = nums1[1:]
                else:
                    ans.append(nums2[0])
                    nums2 = nums2[1:]
            return ans

        ret = []
        if len(nums1)>len(nums2):
            nums1,nums2 = nums2,nums1

        len1,len2 = len(nums1),len(nums2)
        for idx in range(max(0,k-len2),min(k,len1)+1):
            tmp = merge(getmaxarray(nums1,idx),getmaxarray(nums2,k-idx))
            ret = max(tmp,ret)
        return ret


S = Solution()
print S.maxNumber([9, 1, 2, 5, 8, 3],[3, 4, 6, 5],5)