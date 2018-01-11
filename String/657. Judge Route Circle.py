# - * - coding:utf8 - * - -
###########################################
# Author: Tinkle
# E-mail: shutingnjupt@gmail.com
# Name:  Judge Route Circle.py
# Creation Time: 2018/1/11
###########################################
'''
Initially, there is a Robot at position (0, 0). Given a sequence of its moves, judge if this robot makes a circle, which means it moves back to the original place.

The move sequence is represented by a string. And each move is represent by a character. The valid robot moves are R (Right), L (Left), U (Up) and D (down). The output should be true or false representing whether the robot makes a circle.

Example 1:
Input: "UD"
Output: true
Example 2:
Input: "LL"
Output: false
'''
class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        pos_x = 0
        pos_y = 0
        for m in moves:
            if m=='U':
                pos_y+=1
            if m=='D':
                pos_y-=1
            if m=='L':
                pos_x-=1
            if m=='R':
                pos_x+=1
        return pos_x==0 and pos_y==0