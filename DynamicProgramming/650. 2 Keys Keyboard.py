# - * - coding:utf8 - * - -
###########################################
# Author: Tinkle
# E-mail: shutingnjupt@gmail.com
# Name:  2 Keys Keyboard.py
# Creation Time: 2018/1/5
###########################################
'''
Initially on a notepad only one character 'A' is present. You can perform two operations on this notepad for each step:

Copy All: You can copy all the characters present on the notepad (partial copy is not allowed).
Paste: You can paste the characters which are copied last time.
Given a number n. You have to get exactly n 'A' on the notepad by performing the minimum number of steps permitted. Output the minimum number of steps to get n 'A'.

Example 1:
Input: 3
Output: 3
Explanation:
Intitally, we have one character 'A'.
In step 1, we use Copy All operation.
In step 2, we use Paste operation to get 'AA'.
In step 3, we use Paste operation to get 'AAA'.
'''
class Solution(object):
    def minSteps(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <=1:
            return 0
        dp = [0 for i in range(n+1)]
        for i in range(2,n+1):
            dp[i]=i
            for k in range(2,i/2+1):
                if i%k==0:
                    dp[i]=min(dp[i],dp[k]+i/k)
        return dp[-1]
S = Solution()
print S.minSteps(6)