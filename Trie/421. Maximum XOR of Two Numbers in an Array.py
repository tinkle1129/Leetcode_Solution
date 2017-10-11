# - * - coding:utf8 - * - -
###########################################
# Author: Tinkle
# E-mail: shutingnjupt@gmail.com
# Name: Maximum XOR of Two Numbers in an Array.py
# Creation Time: 2017/10/11
###########################################
'''
Given a non-empty array of numbers, a0, a1, a2, … , an-1, where 0 ≤ ai < 231.

Find the maximum result of ai XOR aj, where 0 ≤ i, j < n.

Could you do this in O(n) runtime?

Example:

Input: [3, 10, 5, 25, 2, 8]

Output: 28

Explanation: The maximum result is 5 ^ 25 = 28.
'''
import sys
class Node(object):
    def __init__(self):
        self.val = [None,None]

class Solution(object):
    def findMaximumXOR(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums == [] or len(nums)<2:
            return 0
        root = Node()
        ret = -sys.maxint

        for num in nums:
            tmp = root
            i = 30
            while(i>=0):
                bit = num & (1<<i)
                if bit!=0:
                    bit=1
                if tmp.val[bit]==None:
                    tmp.val[bit]=Node()
                tmp = tmp.val[bit]
                i-=1
            tmp = root
            res = 0
            i = 30
            while(i>=0):
                bit = num & (1<<i)
                if bit !=0:
                    bit = 1
                if tmp.val[1-bit]==None:
                    tmp = tmp.val[bit]
                    res += bit<<i
                else:
                    tmp = tmp.val[1-bit]
                    res += (1-bit)<<i
                i-=1
            ret = max(ret,res^num)
        return ret
    def findMaximumXOR1(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums == [] or len(nums)<2:
            return 0
        root = Node()

        for num in nums:
            tmp = root
            i = 30
            while(i>=0):
                bit = num & (1<<i)
                if bit!=0:
                    bit=1
                if tmp.val[bit]==None:
                    tmp.val[bit]=Node()
                tmp = tmp.val[bit]
                i-=1

        ret = -sys.maxint
        for num in nums:
            tmp = root
            res = 0
            i = 30
            while(i>=0):
                bit = num & (1<<i)
                if bit !=0:
                    bit = 1
                if tmp.val[1-bit]==None:
                    tmp = tmp.val[bit]
                    res += bit<<i
                else:
                    tmp = tmp.val[1-bit]
                    res += (1-bit)<<i
                i-=1
            ret = max(ret,res^num)
        return ret

S = Solution()
print S.findMaximumXOR([3,10,5,25,2,8])