# - * - coding:utf8 - * - -
###########################################
# Author: Tinkle
# E-mail: shutingnupt@gmail.com
# Name: Combinations.py
# Creation Time: 2017/7/11
###########################################
'''
Given two integers n and k, return all possible combinations of k numbers out of 1 ... n.
For example,
If n = 4 and k = 2, a solution is:
[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]
'''
class Solution(object):

    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        ret = []
        candidates_ = [i for i in range(1,n+1)]
        tmp = []
        def dfs(step,candidates,tmp):
            if step == k:
                ret.append(tmp[:])
            elif step == n-k:
                ret.append(list(set(candidates_)-set(tmp[:])))
            else:
                for i in range(len(candidates)):
                    tmp.append(candidates[i])
                    can = candidates[i+1:]
                    dfs(step+1,can,tmp)
                    tmp.pop()
        dfs(0,candidates_,tmp)
        return ret

S = Solution()
print len(S.combine(20,16))