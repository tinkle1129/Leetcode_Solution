# - * - coding:utf8 - * - -
###########################################
# Author: Tinkle
# E-mail: shutingnjupt@gmail.com
# Name: Strong Password Checker.py
# Creation Time: 2017/10/10
###########################################
'''
A password is considered strong if below conditions are all met:

It has at least 6 characters and at most 20 characters.
It must contain at least one lowercase letter, at least one uppercase letter, and at least one digit.
It must NOT contain three repeating characters in a row ("...aaa..." is weak, but "...aa...a..." is strong, assuming other conditions are met).
Write a function strongPasswordChecker(s), that takes a string s as input, and return the MINIMUM change required to make s a strong password. If s is already strong, return 0.

Insertion, deletion or replace of any one character are all considered as one change.
'''


class Solution(object):
    def strongPasswordChecker(self, s):
        """
        :type s: str
        :rtype: int
        """
        totalCnt = len(s)

        lowers = [c for c in s if c.islower()]
        uppers = [c for c in s if c.isupper()]
        digits = [c for c in s if c.isdigit()]

        typeCnt = bool(lowers) + bool(uppers) + bool(digits)

        if totalCnt < 6:
            return max(6 - totalCnt, 3 - typeCnt)

        repeats = []
        dp = [1 for i in range(totalCnt)]
        for i in range(1, totalCnt):
            if s[i] == s[i - 1]:
                dp[i] += dp[i - 1]
            elif dp[i - 1] >= 3:
                repeats.append(dp[i - 1])
        if dp[-1] >= 3:
            repeats.append(dp[-1])

        diff = max(totalCnt - 20, 0)
        res = diff
        for k in range(1, 3):
            idx = 0
            while (idx < len(repeats) and diff > 0):
                if repeats[idx] >= 3 and repeats[idx] % 3 == (k - 1):
                    repeats[idx] -= k
                    diff -= k
                    if diff < 0:
                        res += abs(diff)
                idx += 1

        left = 0
        for i in range(len(repeats)):
            if repeats[i] >= 3 and diff > 0:
                need = repeats[i] - 2
                repeats[i] -= diff
                diff -= need

            if repeats[i] >= 3:
                left += repeats[i] / 3

        res += max(3 - typeCnt, left)
        return res


S = Solution()
#print S.strongPasswordChecker("1111111111")
print S.strongPasswordChecker("aaaaaa1234567890123Ubefg")