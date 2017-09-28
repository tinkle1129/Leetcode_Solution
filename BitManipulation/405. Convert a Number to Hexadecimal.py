# - * - coding:utf8 - * - -
###########################################
# Author: Tinkle
# E-mail: shutingnjupt@gmail.com
# Name: Convert a Number to Hexadecimal.py
# Creation Time: 2017/9/28
###########################################
'''
Given an integer, write an algorithm to convert it to hexadecimal. For negative integer, two’s complement method is used.

Note:

All letters in hexadecimal (a-f) must be in lowercase.
The hexadecimal string must not contain extra leading 0s. If the number is zero, it is represented by a single zero character '0'; otherwise, the first character in the hexadecimal string will not be the zero character.
The given number is guaranteed to fit within the range of a 32-bit signed integer.
You must not use any method provided by the library which converts/formats the number to hex directly.
Example 1:

Input:
26

Output:
"1a"
Example 2:

Input:
-1

Output:
"ffffffff"
'''
class Solution(object):
	def toHex(self, num):
		Array = ['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f']
		if num == 0:
			return '0'
		if num<0:
			num = (-num) ^ 0xffffffff
			num = num +1
		ret = ''
		while(num):
			ret=Array[num%16]+ret
			num = num >>4
		return ret