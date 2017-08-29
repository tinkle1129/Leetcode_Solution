# - * - coding:utf8 - * - -
###########################################
# Author: Tinkle
# E-mail: shutingnjupt@gmail.com
# Name:  Remove Invalid Parentheses.py
# Creation Time: 2017/8/29
###########################################
'''
Remove the minimum number of invalid parentheses in order to make the input string valid. Return all possible results.

Note: The input string may contain letters other than the parentheses ( and ).

Examples:
"()())()" -> ["()()()", "(())()"]
"(a)())()" -> ["(a)()()", "(a())()"]
")(" -> [""]
'''


class Solution(object):
    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        def dfs(s):
            mi = calc(s)
            if mi == 0:
                return [s]
            ans = []

            for x in range(len(s)):
                if s[x] in ['(',')']:
                    q = s[:x]+s[x+1:]
                    if q not in visited and calc(q)<mi:
                        visited.add(q)
                        ans.extend(dfs(q))
            return ans

        def calc(s):
            left = 0;right = 0
            for i in s:
                left +={'(':1,')':-1}.get(i,0)
                right += left<0
                left = max(left,0)
            return left+right
        visited = set([s])
        return dfs(s)
S = Solution()
print S.removeInvalidParentheses("(a)())()")