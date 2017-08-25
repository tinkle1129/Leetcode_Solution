# - * - coding:utf8 - * - -
###########################################
# Author: Tinkle
# E-mail: shutingnjupt@gmail.com
# Name:  Different Ways to Add Parentheses.py
# Creation Time: 2017/8/25
###########################################
'''
Given a string of numbers and operators, return all possible results from computing all the different possible ways to group numbers and operators. The valid operators are +, - and *.


Example 1
Input: "2-1-1".

((2-1)-1) = 0
(2-(1-1)) = 2
Output: [0, 2]


Example 2
Input: "2*3-4*5"

(2*(3-(4*5))) = -34
((2*3)-(4*5)) = -14
((2*(3-4))*5) = -10
(2*((3-4)*5)) = -10
(((2*3)-4)*5) = 10
Output: [-34, -14, -10, -10, 10]
'''


class Solution(object):
    def diffWaysToCompute(self, input):
        """
        :type input: str
        :rtype: List[int]
        """
        ret = []
        for i in range(len(input)):
            if input[i] == '-' or input[i] == '+' or input[i] == '*':
                left = self.diffWaysToCompute(input[:i])
                right = self.diffWaysToCompute(input[i+1:])
                for j in range(len(left)):
                    for k in range(len(right)):
                        if input[i]=='-':
                            ret.append(left[j]-right[k])
                        if input[i]=='+':
                            ret.append(left[j]+right[k])
                        if input[i]=='*':
                            ret.append(left[j]*right[k])
        if len(ret)==0:
            ret.append(int(input))
        return ret

S = Solution()
print S.diffWaysToCompute('2*3-4*5')