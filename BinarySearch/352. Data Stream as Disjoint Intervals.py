# - * - coding:utf8 - * - -
###########################################
# Author: Tinkle
# E-mail: shutingnjupt@gmail.com
# Name: Data Stream as Disjoint Intervals.py
# Creation Time: 2017/9/7
###########################################
'''
Given a data stream input of non-negative integers a1, a2, ..., an, ..., summarize the numbers seen so far as a list of disjoint intervals.

For example, suppose the integers from the data stream are 1, 3, 7, 2, 6, ..., then the summary will be:

[1, 1]
[1, 1], [3, 3]
[1, 1], [3, 3], [7, 7]
[1, 3], [7, 7]
[1, 3], [6, 7]
'''


# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class SummaryRanges(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.ranges = []
    def addNum(self, val):
        """
        :type val: int
        :rtype: void
        """
        if self.ranges == []:
            self.ranges = [Interval(val,val)]
            return
        start = 0
        end = len(self.ranges) - 1
        while (start < end):
            mid = (start + end) / 2
            if self.ranges[mid].end >= val:
                end = mid
            else:
                start = mid + 1
        if val < self.ranges[start].start:
            if start == 0:
                if self.ranges[start].start - val == 1:
                    self.ranges[start].start = val
                else:
                    self.ranges.insert(start, Interval(val,val))
            else:
                if self.ranges[start].start - val == 1 and self.ranges[start - 1].end + 1 == val:
                    self.ranges[start - 1].end = self.ranges[start].end
                    self.ranges.pop(start)
                elif self.ranges[start].start - val == 1:
                    self.ranges[start].start = val
                elif self.ranges[start - 1].end + 1 == val:
                    self.ranges[start - 1].end = val
                else:
                    self.ranges.insert(start,Interval(val,val))
        else:
            if val > self.ranges[start].end:
                if val - 1 == self.ranges[start].end:
                    self.ranges[start].end = val
                else:
                    self.ranges.insert(start + 1, Interval(val,val))


    def getIntervals(self):
        """
        :rtype: List[Interval]
        """
        ret = []
        for num in self.ranges:
            ret +=[[num.start,num.end]]
        return ret



        # Your SummaryRanges object will be instantiated and called as such:
obj = SummaryRanges()
for val in [1, 3, 7, 2, 6]:
    obj.addNum(val)
    print obj.getIntervals()
'''
def getindex(ranges,val):
    start = 0
    end = len(ranges) - 1
    while (start < end):
        mid = (start + end) / 2
        if ranges[mid][1] >= val:
            end = mid
        else:
            start = mid+1
    if val<ranges[start][0]:
        if start==0:
            if ranges[start][0]-val==1:
                ranges[start][0]=val
            else:
                ranges.insert(start,[val,val])
        else:
            if ranges[start][0]-val == 1 and ranges[start-1][1]+1 == val:
                ranges[start-1][1] = ranges[start][1]
                ranges.pop(start)
            elif ranges[start][0]-val == 1:
                ranges[start][0] = val
            elif ranges[start-1][1]+1 == val:
                ranges[start-1][1] = val
            else:
                ranges.insert(start,[val,val])
    else:
        if val>ranges[start][1]:
            if val-1 == ranges[start][1]:
                ranges[start][1]=val
            else:
                ranges.insert(start+1,[val,val])
    return ranges[:]

ranges = [[2,4],[6,6],[7,9],[10,12]]
for i in range(14):
    ans = getindex(ranges,i)
'''