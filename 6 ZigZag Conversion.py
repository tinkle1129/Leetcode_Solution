# - * - coding:utf-8 - * - -
###########################################
# Author: Tinkle
# E-mail: shutingnupt@gmail.com
# Name: ZigZag Conversion.py
# Creation Time: 2017/6/22
###########################################

class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1:
            return s
        ret = ['' for i in range(numRows)]
        col = 0
        step = 1
        for tt in s:
            if col == 0:
                step =1
            if col == numRows - 1:
                step = -1
            ret[col] +=tt
            col +=step
        return ''.join(ret)


S = Solution()
print S.convert("PAYPALISHIRING", 3)