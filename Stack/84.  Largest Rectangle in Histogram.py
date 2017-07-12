# - * - coding:utf8 - * - -
###########################################
# Author: Tinkle
# E-mail: shutingnupt@gmail.com
# Name: Largest Rectangle in Histogram.py
# Creation Time: 2017/7/12
###########################################
'''
Given n non-negative integers representing the histogram's bar height where the width of each bar is 1, find the area of largest rectangle in the histogram.
'''


class Solution(object):
    def largestRectangleArea(self,heights):
        Stack_Numbers = []
        Stack_Index = []
        maxS = 0
        for i in range(len(heights)):
            print Stack_Numbers,Stack_Index,heights[i]
            if Stack_Numbers == []:
                Stack_Numbers.append(heights[i])
                Stack_Index.append(i)
            else:
                if heights[i] >= Stack_Numbers[-1]: #Push to Stack
                    Stack_Numbers.append(heights[i])
                    Stack_Index.append(i)
                else:
                    if heights[i]:
                        for k in range(len(Stack_Numbers)):
                            if Stack_Numbers[k] > heights[i]:
                                temp = Stack_Index[k]
                                for h in range(len(Stack_Numbers)-k):
                                    maxS = max(maxS,(i-Stack_Index[k+h])*Stack_Numbers[k+h])
                                break
                        for h in range(len(Stack_Numbers)-k):
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