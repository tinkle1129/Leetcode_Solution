# - * - coding:utf8 - * - -
###########################################
# Author: Tinkle
# E-mail: shutingnjupt@gmail.com
# Name: Find K Pairs with Smallest Sums.py
# Creation Time: 2017/9/21
###########################################
'''
You are given two integer arrays nums1 and nums2 sorted in ascending order and an integer k.

Define a pair (u,v) which consists of one element from the first array and one element from the second array.

Find the k pairs (u1,v1),(u2,v2) ...(uk,vk) with the smallest sums.

Example 1:
Given nums1 = [1,7,11], nums2 = [2,4,6],  k = 3

Return: [1,2],[1,4],[1,6]

The first 3 pairs are returned from the sequence:
[1,2],[1,4],[1,6],[7,2],[7,4],[11,2],[7,6],[11,4],[11,6]
Example 2:
Given nums1 = [1,1,2], nums2 = [1,2,3],  k = 2

Return: [1,1],[1,1]

The first 2 pairs are returned from the sequence:
[1,1],[1,1],[1,2],[2,1],[1,2],[2,2],[1,3],[1,3],[2,3]
Example 3:
Given nums1 = [1,2], nums2 = [3],  k = 3

Return: [1,3],[2,3]

All possible pairs are returned from the sequence:
[1,3],[2,3]

'''

import heapq
import sys


class Solution(object):
    def kSmallestPairs(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[List[int]]
        """
        heap = []
        maxnum = -sys.maxint
        i = 0
        cnt = 0
        while (i < len(nums1)):
            if cnt < k:
                for j in range(len(nums2)):
                    heapq.heappush(heap, (nums1[i] + nums2[j], [nums1[i], nums2[j]]))
                    maxnum = max(maxnum, nums1[i] + nums2[j])
                    cnt += 1
            else:
                j = 0
                while (j < len(nums2) and nums1[i] + nums2[j] < maxnum):
                    heapq.heappush(heap, (nums1[i] + nums2[j], [nums1[i], nums2[j]]))
                    j += 1
            i += 1

        return list(map(lambda x: x[1], heapq.nsmallest(k, heap)))


S = Solution()
print S.kSmallestPairs([1,7,11],[2,4,6],3)
print S.kSmallestPairs([1,1,2],[1,2,3],2)
print S.kSmallestPairs([0,0,0,0,0],[-3,22,35,56,76],22)
#print S.kSmallestPairs([-476570184,-423568801,-385585840,-375390924,-364630569,-359795128,-281872968,-126410430,-75677925,-54214495,-49178055,-32637211,-32198215,3413177,19045759,62248526,67551536,113606647,155411580,164755463,164781059,203133270,277305105,284913246,285973110,296436629,325431544,357294459,378678394,399786157]
#,[-408663357,-404578641,-376531700,-311642519,-294905976,-232001207,-183530032,-141524508,-115652480,-70696522,-63386299,-54656543,-32316999,29714175,33993996,45020708,62165363,84210823,93905151,102177224,209285622,288668099,328300713,338684779,342861859,384940859,408019604,410097843,458721542,475395296]
#,1000)