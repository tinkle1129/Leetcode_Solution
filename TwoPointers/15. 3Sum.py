###########################################
# Author: Tinkle
# E-mail: shutingnupt@gmail.com
# Name:  3Sum.py
# Creation Time: 2017/6/24
###########################################
'''
Given an array S of n integers, are there elements a, b, c in S such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Note: The solution set must not contain duplicate triplets.

For example, given array S = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]
'''
class Solution(object):
    def threeSum(self,num):
        '''
        :param num: list[int]
        :return: list[list[int]]
        '''
        if len(num)<3:
            return []
        num.sort()
        ret = []
        i = 0
        while(i<len(num)-2):
            j = i+1
            k = len(num)-1
            while j<k:
                if num[i]+num[j]+num[k]>0:
                    k -=1
                elif num[i]+num[j]+num[k]<0:
                    j +=1
                else:
                    ret.append([num[i],num[j],num[k]])
                    j +=1
                    k -=1
                    while(j<k and num[j]==num[j-1]):
                        j +=1
                    while(j<k and num[k]==num[k+1]):
                        k -=1
            while i<(len(num)-2) and num[i]==num[i+1]:
                i +=1
            i +=1
        return ret

S = Solution()
print S.threeSum([-1, 0, 1, 2, -1, -4])