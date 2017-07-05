# - * - coding:utf8 - * - -
###########################################
# Author: Tinkle
# E-mail: shutingnupt@gmail.com
# Name:  Merge Intervals.py
# Creation Time: 2017/7/5
###########################################
'''
Given a collection of intervals, merge all overlapping intervals.

For example,
Given [1,3],[2,6],[8,10],[15,18],
return [1,6],[8,10],[15,18].
'''
# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        intervals = sorted(intervals,key=lambda x:x.start)
        if intervals == []:
            return intervals
        start = intervals[0].start
        end = intervals[0].end
        ret = []
        for i in range(1,len(intervals)):
            if intervals[i].start > end:
                ret.append(Interval(start,end))
                start = intervals[i].start
                end = intervals[i].end
            else:
                end = max(end,intervals[i].end)
        ret.append(Interval(start,end))
        return ret