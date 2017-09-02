# - * - coding:utf8 - * - -
###########################################
# Author: Tinkle
# E-mail: shutingnjupt@gmail.com
# Name:  Power of Three.py
# Creation Time: 2017/9/2
###########################################
'''
Given an integer, write a function to determine if it is a power of three.

Follow up:
Could you do it without using any loop / recursion?

Credits:
Special thanks to @dietpepsi for adding this problem and creating all test cases.


'''
import math
class Solution(object):
    def isPowerOfThree(self, n):
        if n>0:
            a=math.log(n)/math.log(3.0);
        else :
            a=0.5;
        b=round(a,0)
        if abs(a-b)<1e-10:
            return True;
        else:
            return False;