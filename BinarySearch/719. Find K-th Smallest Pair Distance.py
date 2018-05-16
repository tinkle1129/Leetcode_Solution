# - * - coding:utf8 - * - -
###########################################
# Author: Tinkle
# E-mail: shutingnjupt@gmail.com
# Name: Find K-th Smallest Pair Distance.py
# Creation Time: 2018/4/22
###########################################
'''
Given an integer array, return the k-th smallest distance among all the pairs. The distance of a pair (A, B) is defined as the absolute difference between A and B.

Example 1:
Input:
nums = [1,3,1]
k = 1
Output: 0
Explanation:
Here are all the pairs:
(1,3) -> 2
(1,1) -> 0
(3,1) -> 2
Then the 1st smallest distance pair is (1,1), and its distance is 0.
Note:
2 <= len(nums) <= 10000.
0 <= nums[i] < 1000000.
1 <= k <= len(nums) * (len(nums) - 1) / 2.
'''
import collections
import bisect


import collections
import bisect
class Solution(object):
    def smallestDistancePair(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        cnt = collections.Counter(nums)
        keys, vals = [], []
        for key in sorted(cnt):
            keys.append(key)
            vals.append(cnt[key] + (vals and vals[-1] or 0))

        def countNums(val):
            idx = bisect.bisect_right(keys, val)
            if idx: return vals[idx - 1]
            return 0

        def smallerThan(val):
            ans = 0
            for i, key in enumerate(keys):
                ans += (countNums(key + val) - vals[i]) * cnt[key] + cnt[key] * (cnt[key] - 1) / 2
            return ans

        lo = min(keys[x + 1] - keys[x] for x in range(len(keys) - 1)) if max(cnt.values()) == 1 else 0
        hi = keys[-1] - keys[0]

        while lo <= hi:
            mi = (lo + hi) / 2
            if smallerThan(mi) >= k: hi = mi - 1
            else: lo = mi + 1
        return lo

S = Solution()
print S.smallestDistancePair([1,3,1],1)