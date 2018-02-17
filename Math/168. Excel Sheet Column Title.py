###########################################
# Author: Tinkle
# E-mail: shutingnupt@gmail.com
# Name: Excel Sheet Column Title.py
# Creation Time: 2018/1/23
###########################################
'''
Given a positive integer, return its corresponding column title as appear in an Excel sheet.

For example:

    1 -> A
    2 -> B
    3 -> C
    ...
    26 -> Z
    27 -> AA
    28 -> AB
Credits:
Special thanks to @ifanchu for adding this problem and creating all test cases.
'''
class Solution(object):
    def convertToTitle(self, n):
        dict=['Z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y']
        ans=[]
        while n!=0:
            ans.append(dict[n%len(dict)])
            tmp=n%len(dict)
            if tmp==0:
                tmp=len(dict)
            n=(n-tmp)/len(dict)
        ans.reverse()
        s=''.join(ans)
        return s