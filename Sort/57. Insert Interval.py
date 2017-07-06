# - * - coding:utf8 - * - -
###########################################
# Author: Tinkle
# E-mail: shutingnupt@gmail.com
# Name:  Insert Interval.py
# Creation Time: 2017/7/6
###########################################
'''
Given a set of non-overlapping intervals, insert a new interval into the intervals (merge if necessary).

You may assume that the intervals were initially sorted according to their start times.

Example 1:
Given intervals [1,3],[6,9], insert and merge [2,5] in as [1,5],[6,9].

Example 2:
Given [1,2],[3,5],[6,7],[8,10],[12,16], insert and merge [4,9] in as [1,2],[3,10],[12,16].

This is because the new interval [4,9] overlaps with [3,5],[6,7],[8,10].
'''


# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """
        i = 0
        while (i < len(intervals) and intervals[i].start < newInterval.start):
            i = i + 1
        intervals.insert(i, newInterval)
        start = intervals[0].start
        end = intervals[0].end
        ret = []
        for i in range(1, len(intervals)):
            if intervals[i].start > end:
                ret.append(Interval(start, end))
                start = intervals[i].start
                end = intervals[i].end
            else:
                end = max(intervals[i].end, end)
        ret.append(Interval(start, end))
        return ret
