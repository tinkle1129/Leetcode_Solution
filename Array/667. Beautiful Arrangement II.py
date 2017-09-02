# - * - coding:utf8 - * - -
###########################################
# Author: Tinkle
# E-mail: shutingnjupt@gmail.com
# Name:  Beautiful Arrangement II.py
# Creation Time: 2017/9/2
###########################################
'''
Given two integers n and k, you need to construct a list which contains n different positive integers ranging from 1 to n and obeys the following requirement:
Suppose this list is [a1, a2, a3, ... , an], then the list [|a1 - a2|, |a2 - a3|, |a3 - a4|, ... , |an-1 - an|] has exactly k distinct integers.

If there are multiple answers, print any of them.

Example 1:
Input: n = 3, k = 1
Output: [1, 2, 3]
Explanation: The [1, 2, 3] has three different positive integers ranging from 1 to 3, and the [1, 1] has exactly 1 distinct integer: 1.
Example 2:
Input: n = 3, k = 2
Output: [1, 3, 2]
Explanation: The [1, 3, 2] has three different positive integers ranging from 1 to 3, and the [2, 1] has exactly 2 distinct integers: 1 and 2.
'''


class Solution(object):
    def constructArray(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[int]
        """
        res = []
        end = n
        start = 1
        for i in range(k):
            if i%2 == 0:
                res += [start]
                start +=1
            else:
                res += [end]
                end -=1
        if k%2 == 1:
            res += [x for x in range(start,end+1)]
        else:
            out = [x for x in range(start,end+1)]
            out.reverse()
            res += out
        return res

S = Solution()
for k in range(1,7):
    print k,S.constructArray(9,k)