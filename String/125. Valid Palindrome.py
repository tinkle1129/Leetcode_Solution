###########################################
# Author: Tinkle
# E-mail: shutingnupt@gmail.com
# Name:  Valid Palindrome.py
# Creation Time: 2018/1/22
###########################################
'''
Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

For example,
"A man, a plan, a canal: Panama" is a palindrome.
"race a car" is not a palindrome.

Note:
Have you consider that the string might be empty? This is a good question to ask during an interview.

For the purpose of this problem, we define empty string as valid palindrome.
'''
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if not len(s) or len(s)==1:
            return True
        tmp=[]
        for i in s:
            if (ord(i)>=65 and ord(i)<=90) or (ord(i)>=97 and ord(i)<=122) or (ord(i)>=48 and ord(i)<=57):
                tmp.append(i)
        i=0;j=len(tmp)-1
        while(i<j):
            if  (ord(tmp[i])>=48 and ord(tmp[i])<=57) or (ord(tmp[j])>=48 and ord(tmp[j])<=57):
                if tmp[i]!=tmp[j]:
                    return False
            if abs(ord(tmp[i])-ord(tmp[j]))%32!=0:
                return False
            i=i+1;j=j-1
        return True