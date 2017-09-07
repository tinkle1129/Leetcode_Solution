# - * - coding:utf8 - * - -
###########################################
# Author: Tinkle
# E-mail: shutingnjupt@gmail.com
# Name:  Top K Frequent Elements.py
# Creation Time: 2017/9/7
###########################################
'''
Given a non-empty array of integers, return the k most frequent elements.

For example,
Given [1,1,1,2,2,3] and k = 2, return [1,2].

Note:
You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
Your algorithm's time complexity must be better than O(n log n), where n is the array's size.
'''

import heapq
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        dic = {}
        for num in nums:
            dic.setdefault(num,0)
            dic[num]+=1
        heap = []
        for num in dic.keys():
            heapq.heappush(heap,(-dic[num],num))
        ret = []
        for i in range(k):
            ret.append(heapq.heappop(heap)[1])
        return ret

S = Solution()
print S.topKFrequent([1,1,1,2,2,3],2)