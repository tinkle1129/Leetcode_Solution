# - * - coding:utf8 - * - -
###########################################
# Author: Tinkle
# E-mail: shutingnjupt@gmail.com
# Name: Perfect Rectangle.py
# Creation Time: 2017/9/25
###########################################
'''
Given N axis-aligned rectangles where N > 0, determine if they all together form an exact cover of a rectangular region.

Each rectangle is represented as a bottom-left point and a top-right point. For example, a unit square is represented as [1,1,2,2]. (coordinate of bottom-left point is (1, 1) and top-right point is (2, 2)).
'''
import collections
class Solution(object):
    def isRectangleCover(self, rectangles):
        """
        :type rectangles: List[List[int]]
        :rtype: bool
        """
        left = min(x[0] for x in rectangles)
        bottom = min(x[1] for x in rectangles)
        right = max(x[2] for x in rectangles)
        top = max(x[3] for x in rectangles)
        pos = collections.defaultdict(int)
        for i,j,m,n in rectangles:
            A,B,C,D = (i,j),(m,j),(i,n),(m,n)
            for p,q in zip((A,B,C,D),(1,2,4,8)):
                if pos[p]&q:
                    return False
                pos[p]|=q
        for px,py in pos:
            if left<px<right or bottom<py<top:
                if pos[(px,py)] not in [3,5,10,12,15]:
                    return False
        return True

rectangles = [
  [1,1,2,3],
  [1,3,2,4],
  [3,1,4,2],
  [3,2,4,4]
]
S = Solution()
print S.isRectangleCover([[1,1,3,3],[3,1,4,2],[3,2,4,4],[1,3,2,4],[2,3,3,4]])