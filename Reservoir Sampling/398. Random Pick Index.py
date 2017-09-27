# - * - coding:utf8 - * - -
###########################################
# Author: Tinkle
# E-mail: shutingnjupt@gmail.com
# Name: Random Pick Index.py
# Creation Time: 2017/9/27
###########################################
'''
Given an array of integers with possible duplicates, randomly output the index of a given target number. You can assume that the given target number must exist in the array.

Note:
The array size can be very large. Solution that uses too much extra space will not pass the judge.

Example:

int[] nums = new int[] {1,2,3,3,3};
Solution solution = new Solution(nums);

// pick(3) should return either index 2, 3, or 4 randomly. Each index should have equal probability of returning.
solution.pick(3);

// pick(1) should return 0. Since in the array only nums[0] is equal to 1.
solution.pick(1);
'''
import random
import collections
class Solution(object):
    def __init__(self,nums):
        self.nums = nums
    def pick(self, target):
        return random.choice([k for k, v in enumerate(self.nums) if v == target])


class Solution2(object): # MLE
    def __init__(self, nums):
        """

        :type nums: List[int]
        :type numsSize: int
        """
        size = len(nums)
        self.next = [0] * (size + 1)
        self.head = collections.defaultdict(int)
        for i, n in enumerate(nums):
            self.next[i + 1] = self.head[n]
            self.head[n] = i + 1

    def pick(self, target):
        """
        :type target: int
        :rtype: int
        """
        cnt = 0
        idx = self.head[target]
        while idx > 0:
            cnt += 1
            idx = self.next[idx]
        c = int(random.random() * cnt)
        idx = self.head[target]
        for x in range(c):
            idx = self.next[idx]
        return idx - 1