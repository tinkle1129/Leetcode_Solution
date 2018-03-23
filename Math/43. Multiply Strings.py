# - * - coding:utf8 - * - -
###########################################
# Author: Tinkle
# E-mail: shutingnupt@gmail.com
# Name:  Multiply Strings.py
# Creation Time: 2018/3/22
###########################################
class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        s1,s2 = len(num1),len(num2)
        ret = [0] * (s1+s2)
        for i in range(s1):
            for j in range(s2):
                ret[i+j+1]+=int(num1[i])*int(num2[j])
        flag = 0
        ans = ''
        for i in range(s1+s2-1,-1,-1):
            ret[i] = ret[i]+flag
            flag = ret[i]/10
            ret[i] = ret[i]%10
            ans = str(ret[i])+ans
        if flag:
            ans = str(flag)+ans
        pos = True
        a = ''
        for i in range(len(ans)):
            if ans[i]=='0' and pos:
                pass
            else:
                pos = False
                a += ans[i]
        return a if len(a) else '0'


S = Solution()
print S.multiply('9','9')


