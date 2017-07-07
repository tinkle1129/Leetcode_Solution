# - * - coding:utf8 - * - -
###########################################
# Author: Tinkle
# E-mail: shutingnupt@gmail.com
# Name:  Add Binary.py
# Creation Time: 2017/7/7
###########################################
'''
Given two binary strings, return their sum (also a binary string).

For example,
a = "11"
b = "1"
Return "100".
'''
class Solution(object):
    def swap(self,a,b):
        a1,b1=list(a),list(b)
        a1.reverse()
        b1.reverse()
        max_num=max(len(a1),len(b1))
        if len(a1)<max_num:
            a1=a1+['0']*(max_num-len(a1))
        else:
            b1=b1+['0']*(max_num-len(b1))
        return a1,b1
    def addBinary(self, aa, bb):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        ret=[]
        flag=0
        a,b=self.swap(aa,bb)
        for i in range(len(a)):
            tmp=int(a[i])+int(b[i])+flag
            if tmp/2==1:
                flag=1
            else:
                flag=0
            ret.append(str(tmp%2))
        if flag==1:
            ret.append('1')
        ret.reverse()
        return  ''.join(ret)