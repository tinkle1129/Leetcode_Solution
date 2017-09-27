# - * - coding:utf8 - * - -
###########################################
# Author: Tinkle
# E-mail: shutingnjupt@gmail.com
# Name:Binary Watch .py
# Creation Time: 2017/9/27
###########################################
'''
A binary watch has 4 LEDs on the top which represent the hours (0-11), and the 6 LEDs on the bottom represent the minutes (0-59).

Each LED represents a zero or one, with the least significant bit on the right.


For example, the above binary watch reads "3:25".

Given a non-negative integer n which represents the number of LEDs that are currently on, return all possible times the watch could represent.

Example:

Input: n = 1
Return: ["1:00", "2:00", "4:00", "8:00", "0:01", "0:02", "0:04", "0:08", "0:16", "0:32"]
'''
class Solution(object):
	def readBinaryWatch(self,num):
		ret=[]
		for h in range(12):
			for m in range(60):
				if bin(h).count('1')+bin(m).count('1') == num:
					if m<10:
						ret.append(str(h)+':'+'0'+str(m))
					else:
						ret.append(str(h)+':'+str(m))
		return ret
    