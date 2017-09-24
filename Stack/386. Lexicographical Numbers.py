# - * - coding:utf8 - * - -
###########################################
# Author: Tinkle
# E-mail: shutingnjupt@gmail.com
# Name: Lexicographical Numbers.py
# Creation Time: 2017/9/24
###########################################
'''
Given an integer n, return 1 - n in lexicographical order.

For example, given 13, return: [1,10,11,12,13,2,3,4,5,6,7,8,9].

Please optimize your algorithm to use less time and space. The input size may be as large as 5,000,000.
'''
class Solution(object):
    def lexicalOrder(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        ret = []
        stack=[1]
        while(stack):
            item = stack.pop()
            ret.append(item)
            if item<n and item%10<9:
                stack.append(item+1)
            if item*10<=n:
                stack.append(item*10)
        return ret