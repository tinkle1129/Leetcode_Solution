# - * - coding:utf8 - * - -
###########################################
# Author: Tinkle
# E-mail: shutingnjupt@gmail.com
# Name:   Additive Number.py
# Creation Time: 2017/8/30
###########################################
'''
Additive number is a string whose digits can form additive sequence.

A valid additive sequence should contain at least three numbers. Except for the first two numbers, each subsequent number in the sequence must be the sum of the preceding two.

For example:
"112358" is an additive number because the digits can form an additive sequence: 1, 1, 2, 3, 5, 8.

1 + 1 = 2, 1 + 2 = 3, 2 + 3 = 5, 3 + 5 = 8
"199100199" is also an additive number, the additive sequence is: 1, 99, 100, 199.
1 + 99 = 100, 99 + 100 = 199
'''


class Solution(object):
    def isAdditiveNumber(self, num):
        """
        :type num: str
        :rtype: bool
        """
        def check(str_,str1,str2):
            if str_ == '':
                return True
            sum_str = str(int(str1)+int(str2))
            if str_[:len(sum_str)]!=sum_str:
                return False
            return check(str_[len(sum_str):],str2,sum_str)

        for i in range(1,len(num)):
            if i > 1 and num[0] == '0':
                continue
            for j in range(i+1,len(num)):
                if j-i>1 and num[i]=='0':
                    continue
                if check(num[j:],num[:i],num[i:j]):
                    return True
        return False

S = Solution()
print S.isAdditiveNumber('0123')