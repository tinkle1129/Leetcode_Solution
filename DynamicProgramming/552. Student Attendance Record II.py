# - * - coding:utf8 - * - -
###########################################
# Author: Tinkle
# E-mail: shutingnjupt@gmail.com
# Name: Student Attendance Record II.py
# Creation Time: 2018/5/25
###########################################
'''
Given a positive integer n, return the number of all possible attendance records with length n, which will be regarded as rewardable. The answer may be very large, return it after mod 109 + 7.

A student attendance record is a string that only contains the following three characters:

'A' : Absent.
'L' : Late.
'P' : Present.
A record is regarded as rewardable if it doesn't contain more than one 'A' (absent) or more than two continuous 'L' (late).

Example 1:
Input: n = 2
Output: 8
Explanation:
There are 8 records with length 2 will be regarded as rewardable:
"PP" , "AP", "PA", "LP", "PL", "AL", "LA", "LL"
Only "AA" won't be regarded as rewardable owing to more than one absent times.
Note: The value of n won't exceed 100,000.
'''


class Solution(object):
    def checkRecord(self, n):
        """
        :type n: int
        :rtype: int
        """
        MOD = 1000000007
        dp = [[1, 1, 0], [1, 0, 0]]
        for i in range(2, n + 1):
            tmp = sum(dp[0]) % MOD
            dp[0][2] = dp[0][1]
            dp[0][1] = dp[0][0]
            dp[0][0] = tmp

            tmp = (dp[0][0] + sum(dp[1])) % MOD
            dp[1][2] = dp[1][1]
            dp[1][1] = dp[1][0]
            dp[1][0] = tmp

        return (sum(dp[0]) + sum(dp[1])) % MOD

