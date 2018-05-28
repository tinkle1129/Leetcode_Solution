# - * - coding:utf8 - * - -
###########################################
# Author: Tinkle
# E-mail: shutingnjupt@gmail.com
# Name:  Kth Smallest Number in Multiplication Table.py
# Creation Time: 2018/5/28
###########################################
'''
Nearly every one have used the Multiplication Table. But could you find out the k-th smallest number quickly from the multiplication table?

Given the height m and the length n of a m * n Multiplication Table, and a positive integer k, you need to return the k-th smallest number in this table.

Example 1:
Input: m = 3, n = 3, k = 5
Output:
Explanation:
The Multiplication Table:
1	2	3
2	4	6
3	6	9

The 5-th smallest number is 3 (1, 2, 2, 3, 3).
Example 2:
Input: m = 2, n = 3, k = 6
Output:
Explanation:
The Multiplication Table:
1	2	3
2	4	6

The 6-th smallest number is 6 (1, 2, 2, 3, 4, 6).
Note:
The m and n will be in the range [1, 30000].
The k will be in the range [1, m * n]
Seen this question in a real interview before?

'''


class Solution(object):
    def findKthNumber(self, m, n, k):
        """
        :type m: int
        :type n: int
        :type k: int
        :rtype: int
        """
        '''
        (1,1)
        (1,2) (2,1)
        (1,3)       (3,1)
        (1,4) (2,2)       (4,1)
        '''

        count = lambda t: sum(min(m, t / x) for x in range(1, n + 1))
        lo, hi = 1, k
        while lo <= hi:
            mid = (lo + hi) / 2
            if (count(mid)) >= k:
                hi = mid - 1
            else:
                lo = mid + 1
        return lo