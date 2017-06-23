###########################################
# Author: Tinkle
# E-mail: shutingnupt@gmail.com
# Name:  Regular Expression Matching.py
# Creation Time: 2017/6/23
###########################################
"""
'.' Matches any single character.
'*' Matches zero or more of the preceding element.

The matching should cover the entire input string (not partial).

The function prototype should be:
bool isMatch(const char *s, const char *p)

Some examples:
#isMatch("aa","a")  false
#isMatch("aa","aa")   true
#isMatch("aaa","aa")   false
#isMatch("aa", "a*")   true
#isMatch("aa", ".*")   true
#isMatch("ab", ".*")   true
#isMatch("aab", "c*a*b")   true

"""
class Solution(object):
    dic = {}
    def isMatch(self, s, p):
        '''
        :param s: str
        :param p: str
        :return: bool
        '''
        if (s,p) in self.dic:
            return self.dic[(s,p)]
        if p == '':
            return s==''
        if len(p)==1 or p[1]!='*':
            self.dic[(s[1:],p[1:])] = self.isMatch(s[1:],p[1:])
            return len(s)>0 and (p[0]=='.' or p[0]==s[0]) and self.dic[(s[1:],p[1:])]
        while(len(s) and (p[0]=='.' or p[0]==s[0])):
            self.dic[(s,p[2:])] = self.isMatch(s,p[2:])
            if self.isMatch(s[:],p[2:]):
                return True
            s = s[1:]
        self.dic[(s,p[2:])] = self.isMatch(s,p[2:])
        return self.dic[(s,p[2:])]


S = Solution()

print S.isMatch("aa","a")
print S.isMatch("aa","aa")
print S.isMatch("aaa","aa")
print S.isMatch("aa", "a*")
print S.isMatch("aa", ".*")
print S.isMatch("ab", ".*")
print S.isMatch("aab", "c*a*b")
