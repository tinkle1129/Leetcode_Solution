# - * - coding:utf8 - * - -
###########################################
# Author: Tinkle
# E-mail: shutingnjupt@gmail.com
# Name: Decode String.py
# Creation Time: 2017/9/26
###########################################
'''
Given an encoded string, return it's decoded string.

The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. Note that k is guaranteed to be a positive integer.

You may assume that the input string is always valid; No extra white spaces, square brackets are well-formed, etc.

Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, k. For example, there won't be input like 3a or 2[4].

Examples:

s = "3[a]2[bc]", return "aaabcbc".
s = "3[a2[c]]", return "accaccacc".
s = "2[abc]3[cd]ef", return "abcabccdcdcdef".
'''
class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        digit = None
        stack = []
        for si in s:
            if si>='0' and si<='9':
                if digit==None:
                    digit=int(si)
                else:
                    digit=digit*10+int(si)
            elif si=='[':
                if digit!=None:
                    stack.append(digit)
                    digit=None
                stack.append(si)
            elif si==']':
                tmp = ''
                while(stack and stack[-1]!='['):
                    tmp = stack[-1]+tmp
                    stack.pop()
                stack[-1] = tmp
                if len(stack)>1 and isinstance(stack[-2],int):
                    stack[-2] = stack[-2]*stack[-1]
                stack.pop()
            else:
                stack.append(si)
        return ''.join(stack)


S = Solution()
print S.decodeString("2[abc]3[cd]ef")
print S.decodeString("3[a]2[bc]")

print S.decodeString("3[a2[c]]")
print S.decodeString("sd2[f2[e]g]i")