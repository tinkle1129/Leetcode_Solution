###########################################
# Author: Tinkle
# E-mail: shutingnupt@gmail.com
# Name:  Count and Say.py
# Creation Time: 2018/1/21
###########################################
'''
The count-and-say sequence is the sequence of integers with the first five terms as following:

1.     1
2.     11
3.     21
4.     1211
5.     111221
1 is read off as "one 1" or 11.
11 is read off as "two 1s" or 21.
21 is read off as "one 2, then one 1" or 1211.
Given an integer n, generate the nth term of the count-and-say sequence.

Note: Each term of the sequence of integers will be represented as a string.

Example 1:

Input: 1
Output: "1"
Example 2:

Input: 4
Output: "1211"

'''
class Solution(object):
    def show(self,s):
        count=1
        ret=''
        flag=s[0]
        for i in range(1,len(s)):
            if s[i]!=flag:
                ret=ret+str(count)+flag
                flag=s[i]
                count=1
            else:
                count=count+1
        ret=ret+str(count)+flag
        return ret
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        s='1'
        if n==1:
            return s
        else:
            for i in range(2,n+1):
                s=self.show(s)
            return s