# - * - coding:utf8 - * - -
###########################################
# Author: Tinkle
# E-mail: shutingnupt@gmail.com
# Name:  Multiply Strings.py
# Creation Time: 2018/3/22
###########################################
'''
Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2.
Note:
The length of both num1 and num2 is < 110.
Both num1 and num2 contains only digits 0-9.
Both num1 and num2 does not contain any leading zero.
You must not use any built-in BigInteger library or convert the inputs to integer directly.
'''
class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        ##第x位置的值是满足i+j=x的乘积之和加上x-1位的进位

        s1,s2 = len(num1),len(num2)
        ret = [0] * (s1+s2)
        for i in range(s1):
            for j in range(s2):
                ret[i+j+1]+=int(num1[i])*int(num2[j])

        # 处理进位
        flag = 0
        ans = ''
        for i in range(s1+s2-1,-1,-1):
            ret[i] = ret[i]+flag
            flag = ret[i]/10
            ret[i] = ret[i]%10
            ans = str(ret[i])+ans
        if flag:
            ans = str(flag)+ans

        # 处理首字母是0的情况
        pos = True
        a = ''
        for i in range(len(ans)):
            if ans[i]=='0' and pos:
                pass
            else:
                pos = False
                a += ans[i]
        return a if len(a) else '0'