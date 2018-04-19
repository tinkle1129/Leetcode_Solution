# - * - coding:utf8 - * - -
###########################################
# Author: Tinkle
# E-mail: shutingnjupt@gmail.com
# Name:   Fraction Addition and Subtraction.py
# Creation Time: 2018/3/24
###########################################
'''
Given a string representing an expression of fraction addition and subtraction, you need to return the calculation result in string format. The final result should be irreducible fraction. If your final result is an integer, say 2, you need to change it to the format of fraction that has denominator 1. So in this case, 2 should be converted to 2/1.

Example 1:
Input:"-1/2+1/2"
Output: "0/1"
Example 2:
Input:"-1/2+1/2+1/3"
Output: "1/3"
Example 3:
Input:"1/3-1/2"
Output: "-1/6"
Example 4:
Input:"5/3+1/3"
Output: "2/1"
Note:
The input string only contains '0' to '9', '/', '+' and '-'. So does the output.
Each fraction (input and output) has format ±numerator/denominator. If the first input fraction or the output is positive, then '+' will be omitted.
The input only contains valid irreducible fractions, where the numerator and denominator of each fraction will always be in the range [1,10]. If the denominator is 1, it means this fraction is actually an integer in a fraction format defined above.
The number of given fractions will be in the range [1,10].
The numerator and denominator of the final result are guaranteed to be valid and in the range of 32-bit int.
'''
class Solution(object):
    def fractionAddition(self, expression):
        """
        :type expression: str
        :rtype: str
        """

        numerators = []
        product = 1
        products = []
        tmp = []
        c = ''
        for i in expression:
            if (i=='+' or i=='-') and len(c):
                tmp.append(c)
                c=i
            else:
                c+=i
        tmp.append(c)
        for exp in tmp:
            exp = exp.split('/')
            product*=int(exp[1])
            products.append(int(exp[1]))
            numerators.append(int(exp[0]))

        numerator = 0
        for pro,num in zip(products,numerators):
            numerator+=num*(product/pro)
        def gcd(a, b):
            if a < b: a, b = b, a
            while b:
                a, b = b, a % b
            return a
        x = gcd(abs(numerator),abs(product))
        numerator = numerator/x
        product = product/x
        return str(numerator)+'/'+str(product)

S = Solution()
print S.fractionAddition("1/3-1/2")
print S.fractionAddition("-1/2+1/2+1/3")
print S.fractionAddition("-10/7+1/9+2/7+2/1-1/3+3/10-1/10+8/7-4/9-3/2")