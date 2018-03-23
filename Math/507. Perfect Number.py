# - * - coding:utf8 - * - -
###########################################
# Author: Tinkle
# E-mail: shutingnjupt@gmail.com
# Name:   Perfect Number.py
# Creation Time: 2018/3/22
###########################################
'''
We define the Perfect Number is a positive integer that is equal to the sum of all its positive divisors except itself.

Now, given an integer n, write a function that returns true when it is a perfect number and false when it is not.
Example:
Input: 28
Output: True
Explanation: 28 = 1 + 2 + 4 + 7 + 14
Note: The input number n will not exceed 100,000,000. (1e8)
'''
class Solution(object):
    def checkPerfectNumber(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num == 1: return False
        divisors = [1]
        start,end = 2,num
        while(start*start<=num):
            if num%start==0:
                end = num/start
                divisors.append(end)
                divisors.append(start)
            start+=1
        return sum(divisors)==num