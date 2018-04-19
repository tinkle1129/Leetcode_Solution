# - * - coding:utf8 - * - -
###########################################
# Author: Tinkle
# E-mail: shutingnjupt@gmail.com
# Name:   Complex Number Multiplication.py
# Creation Time: 2018/3/23
###########################################
'''
Given two strings representing two complex numbers.

You need to return a string representing their multiplication. Note i2 = -1 according to the definition.

Example 1:
Input: "1+1i", "1+1i"
Output: "0+2i"
Explanation: (1 + i) * (1 + i) = 1 + i2 + 2 * i = 2i, and you need convert it to the form of 0+2i.
Example 2:
Input: "1+-1i", "1+-1i"
Output: "0+-2i"
Explanation: (1 - i) * (1 - i) = 1 + i2 - 2 * i = -2i, and you need convert it to the form of 0+-2i.
Note:

The input strings will not have extra blank.
The input strings will be given in the form of a+bi, where the integer a and b will both belong to the range of [-100, 100]. And the output should be also in this form.
'''


class Solution(object):
    def complexNumberMultiply(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """

        def RealImag(x):
            x = x.split('+')
            return int(x[0]), int(x[1].strip('i'))

        a_realpart, a_imaginarypart = RealImag(a)
        b_realpart, b_imaginarypart = RealImag(b)

        realpart = a_realpart * b_realpart - a_imaginarypart * b_imaginarypart
        imaginarypart = a_realpart * b_imaginarypart + a_imaginarypart * b_realpart

        return str(realpart) + '+' + str(imaginarypart) + 'i'
    