# - * - coding:utf8 - * - -
###########################################
# Author: Tinkle
# E-mail: shutingnjupt@gmail.com
# Name: Integer Replacement.py
# Creation Time: 2017/9/26
###########################################
'''
Given a positive integer n and you can do operations as follow:

If n is even, replace n with n/2.
If n is odd, you can replace n with either n + 1 or n - 1.
What is the minimum number of replacements needed for n to become 1?

Example 1:

Input:
8

Output:
3

Explanation:
8 -> 4 -> 2 -> 1
Example 2:

Input:
7

Output:
4

Explanation:
7 -> 8 -> 4 -> 2 -> 1
or
7 -> 6 -> 3 -> 2 -> 1
'''
class Solution(object):
    def integerReplacement(self,num):
        '''
        :param num:
        :return:
        '''
        cnt = 0
        while(num!=1):
            if num & 1 == 0:
                num = num>>1
            elif (num==3) or (num & 3 !=3):
                num -=1
            else:
                num +=1
            cnt+=1
        return cnt

    def integerReplacement_(self, num):
        dict_ = {}
        dict_[1] = 0

        def dfs(n):
            if n not in dict_.keys():
                if n % 2 == 0:
                    dict_[n] = dfs(n / 2) + 1
                else:
                    dict_[n] = min(dfs(n / 2 + 1), dfs(n / 2)) + 2  # avoid maxInt Value
            return dict_[n]

        return dfs(num)

S = Solution()
print S.integerReplacement(65535)
