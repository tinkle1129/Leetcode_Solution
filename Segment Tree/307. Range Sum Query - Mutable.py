# - * - coding:utf8 - * - -
###########################################
# Author: Tinkle
# E-mail: shutingnjupt@gmail.com
# Name:   Range Sum Query - Mutable.py
# Creation Time: 2017/8/30
###########################################
'''
Given an integer array nums, find the sum of the elements between indices i and j (i ≤ j), inclusive.

The update(i, val) function modifies nums by updating the element at index i to val.
Example:
Given nums = [1, 3, 5]

sumRange(0, 2) -> 9
update(1, 2)
sumRange(0, 2) -> 8
'''


class NumArray(object):
    def __init__(self, nums):
        '''
        :param nums: List[int]
        '''
        self.nums = nums
        self.segTree = [0] * (4 * len(nums) + 10)
        if len(nums):
            self.Build(1, 0, len(nums) - 1)

    def Build(self, node, begin, end):
        if begin == end:
            self.segTree[node] = self.nums[begin]
        else:
            mid = (begin + end) / 2
            self.Build(2 * node, begin, mid)
            self.Build(2 * node + 1, mid + 1, end)

            self.segTree[node] = self.segTree[2 * node] + self.segTree[2 * node + 1]

    def range(self, node, begin, end, i, j):
        if begin >= i and end <= j:
            return self.segTree[node]
        elif end < i or begin > j:
            return 0
        else:
            mid = (begin + end) / 2
            p1 = self.range(2 * node, begin, mid, i, j)
            p2 = self.range(2 * node + 1, mid + 1, end, i, j)
            return p1 + p2

    def sumRange(self, i, j):
        '''
        :param i: int
        :param j: int
        :return: int
        '''
        if i < 0 or j < 0 or i >= len(self.nums) or j >= len(self.nums):
            return 0
        return self.range(1, 0, len(self.nums) - 1, i, j)

    def update(self, i, val):
        '''
        :param i: int
        :param val: int
        :return: void
        '''
        if i < 0 or i >= len(self.nums):
            return
        self.up(1, 0, len(self.nums) - 1, i, val)

    def up(self, node, begin, end, i, val):
        if begin == end:
            self.segTree[node] = val
        else:
            mid = (begin + end) / 2
            if mid >= i:
                self.up(2 * node, begin, mid, i, val)
            else:
                self.up(2 * node + 1, mid + 1, end, i, val)
            self.segTree[node] = self.segTree[2 * node] + self.segTree[2 * node + 1]
