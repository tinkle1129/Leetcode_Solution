# - * - coding:utf8 - * - -
###########################################
# Author: Tinkle
# E-mail: shutingnjupt@gmail.com
# Name:  Largest Rectangle in Histogram.py
# Creation Time: 2018/4/25
###########################################
'''
Given n non-negative integers representing the histogram's bar height where the width of each bar is 1, find the area of largest rectangle in the histogram.
Above is a histogram where width of each bar is 1, given height = [2,1,5,6,2,3].
The largest rectangle is shown in the shaded area, which has area = 10 unit.
Example:
Input: [2,1,5,6,2,3]
Output: 10
'''


class Solution(object):
    def largestRectangleArea(self, heights):
        heights.append(0)
        stack = []
        area = 0
        for i,h in enumerate(heights):
            if stack == [] or heights[stack[-1]]<=h:
                stack.append(i)
            else:
                while(stack and heights[stack[-1]]>h):
                    idx = stack.pop()
                    left = stack[-1] if stack else -1
                    area = max((i-left-1)*heights[idx],area)
                stack.append(i)
        return area

    def largestRectangleArea_(self, heights):
        Stack_Numbers = []
        Stack_Index = []
        maxS = 0
        for i in range(len(heights)):
            if Stack_Numbers == []:
                Stack_Numbers.append(heights[i])
                Stack_Index.append(i)
            else:
                if heights[i] >= Stack_Numbers[-1]:  # Push to Stack
                    Stack_Numbers.append(heights[i])
                    Stack_Index.append(i)
                else:
                    if heights[i]:
                        for k in range(len(Stack_Numbers)):
                            if Stack_Numbers[k] > heights[i]:
                                temp = Stack_Index[k]
                                for h in range(len(Stack_Numbers) - k):
                                    maxS = max(maxS, (i - Stack_Index[k + h]) * Stack_Numbers[k + h])
                                break
                        for h in range(len(Stack_Numbers) - k):
                            Stack_Numbers.pop()
                            Stack_Index.pop()
                        Stack_Numbers.append(heights[i])
                        Stack_Index.append(temp)
                    else:
                        for k in range(len(Stack_Numbers)):
                            maxS = max(maxS, (i - Stack_Index[k]) * Stack_Numbers[k])
                        for k in range(len(Stack_Numbers)):
                            Stack_Numbers.pop()
                            Stack_Index.pop()
        if len(Stack_Numbers):
            for k in range(len(Stack_Numbers)):
                maxS = max(maxS, (len(heights) - Stack_Index[k]) * Stack_Numbers[k])
        return maxS

S = Solution()
print S.largestRectangleArea([2,1,5,6,2,3])