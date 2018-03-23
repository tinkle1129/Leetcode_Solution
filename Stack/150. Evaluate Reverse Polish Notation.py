# - * - coding:utf8 - * - -
###########################################
# Author: Tinkle
# E-mail: shutingnjupt@gmail.com
# Name: Evaluate Reverse Polish Notation.py
# Creation Time: 2018/3/8
###########################################
'''
Evaluate the value of an arithmetic expression in Reverse Polish Notation.

Valid operators are +, -, *, /. Each operand may be an integer or another expression.

Some examples:
  ["2", "1", "+", "3", "*"] -> ((2 + 1) * 3) -> 9
  ["4", "13", "5", "/", "+"] -> (4 + (13 / 5)) -> 6
'''
class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack = []
        for token in tokens:
            if token in ['+', '-', '*', '/']:
                num1 = stack.pop()
                num2 = stack.pop()
                if token == '+':
                    stack.append(num1 + num2)
                elif token == '-':
                    stack.append(num2 - num1)
                elif token == '*':
                    stack.append(num1 * num2)
                else:
                    if num1 * num2 < 0:
                        ans = -(-num2 / num1)
                    else:
                        ans = num2 / num1
                    stack.append(ans)
            else:
                stack.append(int(token))
        return stack[0]
S = Solution()
print S.evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"])
