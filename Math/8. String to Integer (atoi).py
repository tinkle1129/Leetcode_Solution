###########################################
# Author: Tinkle
# E-mail: shutingnupt@gmail.com
# Name: String to Integer.py
# Creation Time: 2017/6/22
###########################################
'''
Implement atoi to convert a string to an integer.

Hint: Carefully consider all possible input cases. If you want a challenge, please do not see below and ask yourself what are the possible input cases.

Notes: It is intended for this problem to be specified vaguely (ie, no given input specs). You are responsible to gather all the input requirements up front.

'''
class Solution(object):
    def output(self,ans,id_sign):
        a=0
        if id_sign==0:
            a=ans
        else:
            a=id_sign*ans
        if a>=2147483647:
            a=2147483647
        if a<=-2147483648:
            a=-2147483648
        return a
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        if not len(str):
            return 0
        id_sign=0
        id_begin=0
        ans=0
        for i in str:
            if i=='+' or i=='-':
                if  id_sign==0:
                    id_sign=44-ord(i)
                    id_begin=1
                else:
                    return 0
            elif i==' ':
                if id_begin!=0:
                    return self.output(ans,id_sign)
            elif ord(i)>=48 and ord(i)<=57:
                ans=ans*10+ord(i)-ord('0')
                id_begin=1
            else:
                return self.output(ans,id_sign)
        return self.output(ans,id_sign)