###########################################
# Author: Tinkle
# E-mail: shutingnupt@gmail.com
# Name:  Largest Number At Least Twice of Others.py
# Creation Time: 2018/1/22
###########################################
'''
In a given integer array nums, there is always exactly one largest element.

Find whether the largest element in the array is at least twice as much as every other number in the array.

If it is, return the index of the largest element, otherwise return -1.

Example 1:
Input: nums = [3, 6, 1, 0]
Output: 1
Explanation: 6 is the largest integer, and for every other number in the array x,
6 is more than twice as big as x.  The index of value 6 is 1, so we return 1.
Example 2:
Input: nums = [1, 2, 3, 4]
Output: -1
Explanation: 4 isn't at least as big as twice the value of 3, so we return -1.
Note:
nums will have a length in the range [1, 50].
Every nums[i] will be an integer in the range [0, 99].

'''


class Solution(object):
    def dominantIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return 0
        if nums[0] > nums[1]:
            firstmax = 0
            secondmax = 1
        else:
            firstmax = 1
            secondmax = 0

        for i in range(2, len(nums)):
            if nums[i] > nums[firstmax]:
                secondmax = firstmax
                firstmax = i
            elif nums[i] > nums[secondmax]:
                secondmax = i
        if nums[secondmax] == 0:
            return firstmax
        return firstmax if nums[firstmax] / nums[secondmax] >= 2 else -1

S = Solution()
print S.dominantIndex([2,0,0,3])
print S.dominantIndex([1,0])