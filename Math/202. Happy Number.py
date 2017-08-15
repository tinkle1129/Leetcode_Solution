# - * - coding:utf8 - * - -
###########################################
# Author: Tinkle
# E-mail: shutingnjupt@gmail.com
# Name: Happy Number.py
# Creation Time: 2017/8/14
###########################################
'''
Write an algorithm to determine if a number is "happy".

A happy number is a number defined by the following process: Starting with any positive integer, replace the number by the sum of the squares of its digits, and repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1. Those numbers for which this process ends in 1 are happy numbers.

Example: 19 is a happy number

1^2 + 9^2 = 82
8^2 + 2^2 = 68
6^2 + 8^2 = 100
1^2 + 0^2 + 0^2 = 1
'''
class Solution(object):
    def isHappy(self, n):
    	if n<1:
    		return False
    	elif n==1:
    		return True
    	hashtable={}
    	while n!=1:
    		if n in hashtable:
    			return False
    		else:
    			hashtable.setdefault(n,None)
    			array=[]
    			while n:
    				array.append((n%10)**2)
    				n=n/10
    			n=sum(array)
    	return True
