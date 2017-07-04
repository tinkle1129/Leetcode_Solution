# - * - coding:utf8 - * - -
###########################################
# Author: Tinkle
# E-mail: shutingnupt@gmail.com
# Name:  Trapping Rain Water.py
# Creation Time: 2017/7/1
###########################################
'''
Given n non-negative integers representing an elevation map where the width of each bar is 1,
 compute how much water it is able to trap after raining.

For example,
Given [0,1,0,2,1,0,1,3,2,1,2,1], return 6.
'''


class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if len(height)<3:
            return 0
        peak = []
        ret = 0
        for i in range(len(height)):
            if i == 0 or i == len(height)-1:
                peak.append(i)
            else:
                if height[i]>=height[i-1] and height[i]>height[i+1]:
                    peak.append(i)
        stack = []
        curheight = 0
        for i in range(len(peak)):

            if i == 0:
                stack.append(peak[i])
                curheight = max(curheight,height[peak[i]])
            else:
                if height[peak[i]]<=height[stack[-1]]:
                    stack.append(peak[i])
                    curheight = max(curheight, height[peak[i]])
                else:
                    while(len(stack)>1 and height[peak[i]]>height[stack[-1]] and height[stack[-1]]!=curheight):
                        stack.pop()
                    stack.append(peak[i])
                    curheight = max(curheight, height[peak[i]])
        for i in range(1,len(stack)):
            start = stack[i-1]
            end = stack[i]
            maxheight = min(height[start],height[end])
            for idx in range(start+1,end):
                ret += max(maxheight-height[idx],0)
        return ret

S = Solution()
print S.trap([0,1,0,2,1,0,1,3,2,1,2,1])
print S.trap([5,4,1,2])
print S.trap([5,2,1,2,1,5])
print S.trap([6,4,2,0,3,2,0,3,1,4,5,3,2,7,5,3,0,1,2,1,3,4,6,8,1,3])
print S.trap([5,3,7,7])