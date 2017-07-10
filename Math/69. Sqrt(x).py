# - * - coding:utf8 - * - -
###########################################
# Author: Tinkle
# E-mail: shutingnupt@gmail.com
# Name:  Sqrt(x).py
# Creation Time: 2017/7/10
###########################################
'''
Implement int sqrt(int x).

Compute and return the square root of x.
'''
class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        start=0
        end=(x+1)/2
        while(start<end):
            mid=start+(end-start)/2
            tmp=mid*mid
            if(tmp==x):
                return mid
            elif tmp<x:
                start=mid+1
            else:
                end=mid-1
        tmp=end*end
        if(tmp>x):
            return end-1
        else:
            return end