###########################################
# Author: Tinkle
# E-mail: shutingnupt@gmail.com
# Name:  Integer to Roman.py
# Creation Time: 2017/6/23
###########################################
'''
Given an integer, convert it to a roman numeral.
Input is guaranteed to be within the range from 1 to 3999.
'''
class Solution(object):
    def intToRoman(self,num):
        '''
        :param num:int
        :return:str
        '''
        translation = [['','I','II','III','IV','V','VI','VII','VIII','IX'],
                       ['','X','XX','XXX','XL','L','LX','LXX','LXXX','XC'],
                       ['','C','CC','CCC','CD','D','DC','DCC','DCCC','CM'],
                       ['','M','MM','MMM']]
        s = ''
        digit = 1000
        i = 3
        while(num%digit!=0):
            tmp = num/digit
            s = s+translation[i][tmp]
            num = num%digit
            digit /=10
            i = i-1
        s +=translation[i][num/digit]
        return s

S = Solution()
print S.intToRoman(10)