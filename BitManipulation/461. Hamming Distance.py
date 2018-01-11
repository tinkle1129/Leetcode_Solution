# - * - coding:utf8 - * - -
###########################################
# Author: Tinkle
# E-mail: shutingnjupt@gmail.com
# Name:  Hamming Distance.py
# Creation Time: 2018/1/11
###########################################
'''
The Hamming distance between two integers is the number of positions at which the corresponding bits are different.

Given two integers x and y, calculate the Hamming distance.

Note:
0 ≤ x, y < 231.

Example:

Input: x = 1, y = 4

Output: 2

Explanation:
1   (0 0 0 1)
4   (0 1 0 0)
       ↑   ↑

The above arrows point to positions where the corresponding bits are different.
'''
class Solution(object):
    def hammingDistance(self, x, y):
        ret=0
        ans=x ^ y
        while(ans):
            ret = ret+ans % 2
            ans = ans>>1
        return ret