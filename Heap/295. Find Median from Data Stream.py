# - * - coding:utf8 - * - -
###########################################
# Author: Tinkle
# E-mail: shutingnjupt@gmail.com
# Name:  Find Median from Data Stream.py
# Creation Time: 2017/8/27
###########################################
'''
Median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value. So the median is the mean of the two middle value.

Examples:
[2,3,4] , the median is 3

[2,3], the median is (2 + 3) / 2 = 2.5

Design a data structure that supports the following two operations:

void addNum(int num) - Add a integer number from the data stream to the data structure.
double findMedian() - Return the median of all elements so far.
For example:

addNum(1)
addNum(2)
findMedian() -> 1.5
addNum(3)
findMedian() -> 2
'''


class MedianFinder(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.length = 0
        self.array = []

    def addNum(self, num):
        """
        :type num: int
        :rtype: void
        """
        if self.length == 0:
            self.array.append(num)
        else:
            if self.array[0]>num:
                self.array.insert(0,num)
            else:
                start = 0
                end = self.length
                while(start<end-1):
                    mid = (start+end)/2
                    if num == self.array[mid]:
                        start = mid
                        break
                    if num>self.array[mid]:
                        start = mid
                    else:
                        end = mid
                self.array.insert(start+1,num)
        self.length+=1

    def findMedian(self):
        """
        :rtype: float
        """
        if self.length == 0:
            return 0
        else:
            if self.length%2==0:
                left = (self.length-1)/2
                right = left+1
                return float(self.array[left]+self.array[right])/2
            else:
                return float(self.array[(self.length-1)/2])

'''
from heapq import *

class MedianFinder:

    def __init__(self):
        self.heaps = [], []

    def addNum(self, num):
        small, large = self.heaps
        heappush(small, -heappushpop(large, num))
        if len(large) < len(small):
            heappush(large, -heappop(small))

    def findMedian(self):
        small, large = self.heaps
        if len(large) > len(small):
            return float(large[0])
        return (large[0] - small[0]) / 2.0
'''
        # Your MedianFinder object will be instantiated and called as such:
obj = MedianFinder()
obj.addNum(2)
obj.addNum(1)
obj.addNum(4)

print obj.array
print obj.findMedian()
obj.addNum(10)
print obj.array
print obj.findMedian()