# - * - coding:utf8 - * - -
###########################################
# Author: Tinkle
# E-mail: shutingnjupt@gmail.com
# Name:Prime Number of Set Bits in Binary Representation.py
# Creation Time: 2018/1/20
###########################################
'''
Given two integers L and R, find the count of numbers in the range [L, R] (inclusive) having a prime number of set bits in their binary representation.

(Recall that the number of set bits an integer has is the number of 1s present when written in binary. For example, 21 written in binary is 10101 which has 3 set bits. Also, 1 is not a prime.)

Example 1:

Input: L = 6, R = 10
Output: 4
Explanation:
6 -> 110 (2 set bits, 2 is prime)
7 -> 111 (3 set bits, 3 is prime)
9 -> 1001 (2 set bits , 2 is prime)
10->1010 (2 set bits , 2 is prime)
Example 2:

Input: L = 10, R = 15
Output: 5
Explanation:
10 -> 1010 (2 set bits, 2 is prime)
11 -> 1011 (3 set bits, 3 is prime)
12 -> 1100 (2 set bits, 2 is prime)
13 -> 1101 (3 set bits, 3 is prime)
14 -> 1110 (3 set bits, 3 is prime)
15 -> 1111 (4 set bits, 4 is not prime)
'''


class Solution(object):
    def __init__(self):
        MAXN = 1000
        self.prime = [1] * (MAXN + 1)
        self.prime[0] = self.prime[1] = 0
        for i in range(2, MAXN + 1):
            if self.prime[i] == 1:
                for y in range(i * i, MAXN + 1, i):
                    self.prime[y] = 0

    def countPrimeSetBits(self, L, R):
        """
        :type L:
        :type R:
        :rtype:
        """
        ans = 0
        for x in range(L, R + 1):
            ans += self.prime[bin(x).count('1')]
        return ans