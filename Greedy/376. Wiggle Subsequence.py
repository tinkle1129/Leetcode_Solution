# - * - coding:utf8 - * - -
###########################################
# Author: Tinkle
# E-mail: shutingnjupt@gmail.com
# Name: Wiggle Subsequence.py
# Creation Time: 2017/9/21
###########################################
'''
A sequence of numbers is called a wiggle sequence if the differences between successive numbers strictly alternate between positive and negative. The first difference (if one exists) may be either positive or negative. A sequence with fewer than two elements is trivially a wiggle sequence.

For example, [1,7,4,9,2,5] is a wiggle sequence because the differences (6,-3,5,-7,3) are alternately positive and negative. In contrast, [1,4,7,2,5] and [1,7,4,5,5] are not wiggle sequences, the first because its first two differences are positive and the second because its last difference is zero.

Given a sequence of integers, return the length of the longest subsequence that is a wiggle sequence. A subsequence is obtained by deleting some number of elements (eventually, also zero) from the original sequence, leaving the remaining elements in their original order.

Examples:
Input: [1,7,4,9,2,5]
Output: 6
The entire sequence is a wiggle sequence.

Input: [1,17,5,10,13,15,10,5,16,8]
Output: 7
There are several subsequences that achieve this length. One is [1,17,10,13,10,16,8].

Input: [1,2,3,4,5,6,7,8,9]
Output: 2
Follow up:
Can you do it in O(n) time?
'''


class Solution(object):
    def wiggleMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        new_nums = []
        for num in nums:
            if new_nums == [] or num!=new_nums[-1]:
                new_nums.append(num)
        if new_nums == []:
            return 0
        if len(new_nums)==1:
            return 1
        cnt = 2
        if new_nums[1]>new_nums[0]:
            flag = 1
        else:
            flag = 0
        for i in range(2,len(new_nums)):
            if flag==1 and new_nums[i]<new_nums[i-1]:
                flag = 0
                cnt+=1
            elif flag ==0 and new_nums[i]>new_nums[i-1]:
                flag = 1
                cnt+=1
        return cnt




S = Solution()
print S.wiggleMaxLength([0,0,0])
print S.wiggleMaxLength([1,7,4,9,2,5])
print S.wiggleMaxLength([1,2,3,4,5,6,7,8,9])
print S.wiggleMaxLength([1,17,5,10,13,15,10,5,16,8])


