###########################################
# Author: Tinkle
# E-mail: shutingnupt@gmail.com
# Name:  Factorial Trailing Zeroes.py
# Creation Time: 2018/1/23
###########################################
'''
Given an integer n, return the number of trailing zeroes in n!.

Note: Your solution should be in logarithmic time complexity.

Credits:
Special thanks to @ts for adding this problem and creating all test cases.
'''
class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        count=0
        tmp=5
        while(n/tmp):
            count=count+n/tmp
            tmp=tmp*5
        return count