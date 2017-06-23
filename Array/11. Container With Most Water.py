###########################################
# Author: Tinkle
# E-mail: shutingnupt@gmail.com
# Name:  Container With Most Water.py
# Creation Time: 2017/6/23
###########################################
'''
Given n non-negative integers a1, a2, ..., an, where each represents a point at coordinate (i, ai).
n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). Find two lines,
which together with x-axis forms a container, such that the container contains the most water.
Note: You may not slant the container and n is at least 2.
'''
class Solution(object):
    def maxArea(self,height):
        '''
        :param height: list[(int,int)]
        :return: int
        '''
        ma = 0
        start = 0
        end = len(height)-1
        while(start<end):
            ma = max(ma,min(height[start],height[end])*(end-start))
            if(height[start]<height[end]):
                k = start
                while(k<end and height[k]<=height[start]):
                    k = k+1
                start = k
            else:
                k = end
                while(k>start and height[k]<=height[end]):
                    k = k-1
                end = k
        return ma

S = Solution()
print S.maxArea([1,1])