# - * - coding:utf8 - * - -
###########################################
# Author: Tinkle
# E-mail: shutingnupt@gmail.com
# Name: Remove Duplicates from Sorted Array II.py
# Creation Time: 2017/7/11
###########################################
'''
Follow up for "Remove Duplicates":
What if duplicates are allowed at most twice?

For example,
Given sorted array nums = [1,1,1,2,2,3],

Your function should return length = 5, with the first five elements of nums being 1, 1, 2, 2 and 3. It doesn't matter what you leave beyond the new length.

'''
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums):
            j = 0
            count = 1
            for i in range(1,len(nums)):
                if nums[i]==nums[j]:
                    if count == 2:
                         continue
                    else:
                        count +=1
                        j +=1
                        nums[j]=nums[i]
                else:
                    j +=1
                    count = 1
                    nums[j]=nums[i]
            return j+1
        else:
            return 0