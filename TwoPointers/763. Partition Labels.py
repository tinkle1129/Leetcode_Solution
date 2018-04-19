###########################################
# Author: Tinkle
# E-mail: shutingnupt@gmail.com
# Name:  Partition Labels.py
# Creation Time: 2018/4/18
###########################################
'''
A string S of lowercase letters is given. We want to partition this string into as many parts as possible so that each letter appears in at most one part, and return a list of integers representing the size of these parts.

Example 1:
Input: S = "ababcbacadefegdehijhklij"
Output: [9,7,8]
Explanation:
The partition is "ababcbaca", "defegde", "hijhklij".
This is a partition so that each letter appears in at most one part.
A partition like "ababcbacadefegde", "hijhklij" is incorrect, because it splits S into less parts.
Note:

S will have length in range [1, 500].
S will consist of lowercase letters ('a' to 'z') only.
'''
class Solution(object):
    def partitionLabels(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        stack = []
        maps = dict()
        for i,s in enumerate(S):
            if s not in maps:
                maps[s] = i
                stack.append([i,i])
            else:
                idx = maps[s]
                while(stack):
                    [start,end] = stack.pop()
                    if idx>=start:
                        break
                stack.append([start,i])
        ret = []
        for i in stack:
            ret.append(i[1]-i[0]+1)
        return ret