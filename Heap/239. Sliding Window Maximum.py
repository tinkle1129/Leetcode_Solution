# - * - coding:utf8 - * - -
###########################################
# Author: Tinkle
# E-mail: shutingnjupt@gmail.com
# Name:  Sliding Window Maximum.py
# Creation Time: 2017/8/25
###########################################
'''
Given an array nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position.

For example,
Given nums = [1,3,-1,-3,5,3,6,7], and k = 3.

Window position                Max
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7
Therefore, return the max sliding window as [3,3,5,5,6,7].

Note:
You may assume k is always valid, ie: 1 ≤ k ≤ input array's size for non-empty array.

Follow up:
Could you solve it in linear time?
'''


class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        ret = []
        queue = []
        if nums==[]:
            return ret
        for i in range(k):
            if len(queue)==0:
                queue.append((nums[i],i))
            else:
                while(len(queue) and queue[-1][0]<nums[i]):
                    queue.pop()
                queue.append((nums[i],i))
        ret.append(queue[0][0])
        for i in range(k,len(nums)):
            #print queue
            while(len(queue) and i-queue[0][1]>=k):
                queue.pop(0)
            while(len(queue) and queue[-1][0]<nums[i]):
                queue.pop()
            queue.append((nums[i],i))
            ret.append(queue[0][0])
        return ret


S = Solution()
print S.maxSlidingWindow([1,3,-1,-3,5,3,6,7],3)
print S.maxSlidingWindow([1,-1],1)
print S.maxSlidingWindow([1,3,1,2,0,5],3)