# - * - coding:utf8 - * - -
###########################################
# Author: Tinkle
# E-mail: shutingnupt@gmail.com
# Name:  Wildcard Matching.py
# Creation Time: 2017/7/2
###########################################
class Solution(object):
    def isMatch(self,s,p):
        pPointer = sPointer = ss = 0; star = -1
        while(sPointer<len(s)):
            if pPointer<len(p) and (s[sPointer]== p[pPointer] or p[pPointer] == '?'):
                sPointer += 1 ; pPointer +=1
                continue
            if pPointer<len(p) and p[pPointer] == '*':
                star = pPointer; pPointer +=1 ; ss = sPointer
                continue
            if star !=-1:
                pPointer = star+1;ss+=1;sPointer = ss
                continue
            return False
        while pPointer<len(p) and p[pPointer] == '*':
            pPointer +=1
        return pPointer == len(p)
    def isMatch_(self, s, p):
        pPointer=sPointer=ss=0; star=-1
        while sPointer<len(s):
            print sPointer,pPointer,star,ss
            if pPointer<len(p) and (s[sPointer]==p[pPointer] or p[pPointer]=='?'):
                sPointer+=1; pPointer+=1
                continue
            if pPointer<len(p) and p[pPointer]=='*':
                star=pPointer; pPointer+=1; ss=sPointer;
                continue
            if star!=-1:
                pPointer=star+1; ss+=1; sPointer=ss
                continue
            return False
        while pPointer<len(p) and p[pPointer]=='*':
            pPointer+=1
        if pPointer==len(p): return True
        return False
S =Solution()
print S.isMatch('aaaaabcb','a*b')
'''
print S.isMatch('a','a*')
print S.isMatch("aa","a") # F
print S.isMatch("aa","aa") # T
print S.isMatch("aaa","aa") # F
print S.isMatch("aa", "*") # T
print S.isMatch("aa", "a*") # T
print S.isMatch("ab", "?*") # T
print S.isMatch("aab", "c*a*b") # F
print S.isMatch("zacabz","*a?b*") # F
print S.isMatch('a','a*')#T


print S.isMatch("abbaaababaaaabaaaaabaabbabababbaaabaaabaabaaaabbababaaaabababaabababbbbaabaabbbbbaababbbbbbbbaaababbbabbbbaabbbababbbabababbaabaaabaaabbbbbabaaaababababbbaabbaabbabbbaabbbaabaabaabbaabbbbbabbaabbbaabbb",
"***a****a***a*bba*a**aba******b**a*a*b***aa***b*ab*ab*aab*ab*b*abbaa***b**a*bb*b*ab*a*abba**bb*****a")
print S.isMatch("aabbbbaababbabababaabbbbabbabbaabbbabbbabaabbaaaababababbababbabbbbabaaabaaabaabbaaaabbbbabaaabbbbbabbbaabbbbbabaabababaaabaaababaababbaaabaabbabaababbabababaaababbabbabaabbbbabbbbabaabbaababaaabababbab",
"a*b*a*b*aaaa*abaaa**b*a***b*a*bb****ba*ba*b******a********a**baba*ab***a***bbba*b**a*b*ba*a*aaaa*ab**")
'''