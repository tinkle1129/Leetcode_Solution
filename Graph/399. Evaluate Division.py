# - * - coding:utf8 - * - -
###########################################
# Author: Tinkle
# E-mail: shutingnjupt@gmail.com
# Name: Evaluate Division.py
# Creation Time: 2017/9/27
###########################################
'''
Equations are given in the format A / B = k, where A and B are variables represented as strings, and k is a real number (floating point number). Given some queries, return the answers. If the answer does not exist, return -1.0.

Example:
Given a / b = 2.0, b / c = 3.0.
queries are: a / c = ?, b / a = ?, a / e = ?, a / a = ?, x / x = ? .
return [6.0, 0.5, -1.0, 1.0, -1.0 ].

The input is: vector<pair<string, string>> equations, vector<double>& values, vector<pair<string, string>> queries , where equations.size() == values.size(), and the values are positive. This represents the equations. Return vector<double>.

According to the example above:

equations = [ ["a", "b"], ["b", "c"] ],
values = [2.0, 3.0],
queries = [ ["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"] ].
The input is always valid. You may assume that evaluating the queries will result in no division by zero and there is no contradiction.
'''

import collections
class Solution(object):
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        dic = collections.defaultdict(lambda: collections.defaultdict(int))
        for (s,t),v in zip(equations,values):
            dic[s][t] = v
            dic[t][s] = 1.0/v
        for k in dic:
            dic[k][k] = 1
            for s in dic:
                for t in dic:
                    if dic[s][k] and dic[k][t]:
                        dic[s][t] = dic[s][k]*dic[k][t]
        ans = []
        for s,t in queries:
            ans.append(dic[s][t] if dic[s][t] else -1.0)
        return ans

S = Solution()
print S.calcEquation([ ["a", "b"], ["b", "c"] ])
