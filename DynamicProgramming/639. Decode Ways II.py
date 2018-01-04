# - * - coding:utf8 - * - -
###########################################
# Author: Tinkle
# E-mail: shutingnjupt@gmail.com
# Name:  Decode Ways II.py
# Creation Time: 2018/1/4
###########################################
'''
A message containing letters from A-Z is being encoded to numbers using the following mapping way:

'A' -> 1
'B' -> 2
...
'Z' -> 26
Beyond that, now the encoded string can also contain the character '*', which can be treated as one of the numbers from 1 to 9.

Given the encoded message containing digits and the character '*', return the total number of ways to decode it.

Also, since the answer may be very large, you should return the output mod 109 + 7.

Example 1:
Input: "*"
Output: 9
Explanation: The encoded message can be decoded to the string: "A", "B", "C", "D", "E", "F", "G", "H", "I".
Example 2:
Input: "1*"
Output: 9 + 9 = 18
Note:
The length of the input string will fit in range [1, 105].
The input string will only contain the character '*' and digits '0' - '9'.

'''
class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        dp = [1 for i in range(len(s)+1)]

        for i in range(len(s)):
            pos = i+1
            if i == 0:
                if s[i]=='0':
                    return 0
                if s[i]=='*':
                    dp[pos]=9
            else:
                if s[i]=='0':
                    if (s[i-1]>='3' and s[i-1]<='9') or s[i-1]=='0':
                        return 0
                    elif s[i-1]=='*':
                        dp[pos] = dp[pos-2]*2
                    else:
                        dp[pos] = dp[pos-2]
                elif s[i]>='1' and s[i]<='6':
                    if s[i-1]=='1' or s[i-1]=='2':
                        dp[pos] = dp[pos-1]+dp[pos-2]
                    elif s[i-1] == '*':
                        dp[pos] = dp[pos-1] + 2*dp[pos-2]
                    else:
                        dp[pos] = dp[pos-1]
                elif s[i]>='7' and s[i]<='9':
                    if s[i-1]=='1' or s[i-1]=='*':
                        dp[pos] = dp[pos-1]+dp[pos-2]
                    else:
                        dp[pos] = dp[pos-1]
                else:
                    if s[i-1]=='1':
                        dp[pos] = 9*dp[pos-1]+dp[pos-2]*9
                    elif s[i-1] == '2':
                        dp[pos] = 9*dp[pos-1]+dp[pos-2]*6
                    elif s[i-1]=='*':
                        dp[pos] = 9*dp[pos-1]+dp[pos-2]*15
                    else:
                        dp[pos] = 9*dp[pos-1]
            dp[pos] = dp[pos] % (10**9 + 7)
        return dp[-1]

S = Solution()
print S.numDecodings('1*2')