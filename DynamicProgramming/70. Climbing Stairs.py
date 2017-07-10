# - * - coding:utf8 - * - -
###########################################
# Author: Tinkle
# E-mail: shutingnupt@gmail.com
# Name: Climbing Stairs.py
# Creation Time: 2017/7/10
###########################################
'''
You are climbing a stair case. It takes n steps to reach to the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
'''
class Solution(object):
    def climbStairs(self, n):
        #s[n]=s[n-1]+s[n-2]
        if n==1 or n==2:
            return n
        i=3;s=[1,2]
        while(i<=n):
            s.append(s[i-2]+s[i-3])
            i=i+1
        return s.pop()