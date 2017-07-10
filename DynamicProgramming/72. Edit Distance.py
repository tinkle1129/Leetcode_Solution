# - * - coding:utf8 - * - -
###########################################
# Author: Tinkle
# E-mail: shutingnupt@gmail.com
# Name: Edit Distance.py
# Creation Time: 2017/7/10
###########################################
'''
Given two words word1 and word2, find the minimum number of steps required to convert word1 to word2. (each operation is counted as 1 step.)

You have the following 3 operations permitted on a word:

a) Insert a character
b) Delete a character
c) Replace a character
'''
class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        n1=len(word1);n2=len(word2)
        tmp=[0 for i in range(n2+1)]
        ret=[tmp[:] for i in range(n1+1)]
        for i in range(n1+1):
            ret[i][0]=i
        for j in range(n2+1):
            ret[0][j]=j
        for i in range(n1):
            for j in range(n2):
                if word1[i]==word2[j]:
                    ret[i+1][j+1]=ret[i][j]
                else:
                    ret[i+1][j+1]=min(ret[i][j],ret[i][j+1],ret[i+1][j])+1
        return ret[n1][n2]