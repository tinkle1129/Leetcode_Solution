# - * - coding:utf8 - * - -
###########################################
# Author: Tinkle
# E-mail: shutingnjupt@gmail.com
# Name:  Fizz Buzz.py
# Creation Time: 2017/10/9
###########################################
'''
Given a non-empty array of integers, return the third maximum number in this array. If it does not exist, return the maximum number. The time complexity must be in O(n).

Example 1:
Input: [3, 2, 1]

Output: 1

Explanation: The third maximum is 1.
Example 2:
Input: [1, 2]

Output: 2

Explanation: The third maximum does not exist, so the maximum (2) is returned instead.
Example 3:
Input: [2, 2, 3, 1]

Output: 1

Explanation: Note that the third maximum here means the third maximum distinct number.
Both numbers with value 2 are both considered as second maximum.
'''


class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        stack = []
        for num in nums:
            if num not in stack:
                idx = None
                for i in range(len(stack)):
                    if stack[i] < num:
                        idx = i
                        break
                if idx != None:
                    stack.insert(idx, num)
                else:
                    stack.append(num)
                if len(stack) > 3:
                    stack.pop()
        if len(stack) == 3:
            return stack[-1]
        else:
            return stack[0]
