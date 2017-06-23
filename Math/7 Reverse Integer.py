# - * - coding:utf-8 - * - -
###########################################
# Author: Tinkle
# E-mail: shutingnupt@gmail.com
# Name: Reverse integer.py
# Creation Time: 2017/6/22
###########################################
'''
Reverse digits of an integer.

Example1: x = 123, return 321
Example2: x = -123, return -321

click to show spoilers.

Have you thought about this?
Here are some good questions to ask before coding. Bonus points for you if you have already thought through this!

If the integer's last digit is 0, what should the output be? ie, cases such as 10, 100.

Did you notice that the reversed integer might overflow? Assume the input is a 32-bit integer, then the reverse of 1000000003 overflows. How should you handle such cases?

For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.


'''
class Solution(object):
    def reverse(self,x):
        '''
        :param x: int
        :return: int
        '''
        sign = 1
        if x<0:
            sign = -1
            x = -x
        ret = 0
        while(x!=0):
            ret = ret*10+x%10
            x = x/10
        ret = sign*ret
        return ret if ret < 2**31-1 and ret >= -1*(2**31) else 0

S = Solution()
print S.reverse(-10000000000003)