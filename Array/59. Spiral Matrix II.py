# - * - coding:utf8 - * - -
###########################################
# Author: Tinkle
# E-mail: shutingnupt@gmail.com
# Name:  Spiral Matrix II.py
# Creation Time: 2017/7/6
###########################################
'''
Given an integer n, generate a square matrix filled with elements from 1 to n2 in spiral order.

For example,
Given n = 3,

You should return the following matrix:
[
 [ 1, 2, 3 ],
 [ 8, 9, 4 ],
 [ 7, 6, 5 ]
]

'''
class Solution():
    def generateMatrix(self,n):
        ans = [[0 for i in range(n)] for j in range(n)]
        #print ans
        upper_i =0;lower_i=n-1;left_j=0;right_j=n-1
        num=1
        i=0;j=0
        right_pointer=1
        down_pointer=0
        while(num<=n*n):
            ans[i][j]=num
            if right_pointer==1:
                if j<right_j:
                    j=j+1
                else:
                    right_pointer=0
                    down_pointer=1
                    upper_i = upper_i+1
                    i = i+1
            elif down_pointer == 1:
                if i<lower_i:
                    i = i+1
                else:
                    right_pointer=-1
                    down_pointer=0
                    right_j = right_j -1
                    j = j-1
            elif right_pointer ==-1:
                if j > left_j:
                    j=j-1
                else:
                    right_pointer=0
                    down_pointer=-1
                    lower_i =lower_i-1
                    i = i-1
            elif down_pointer == -1:
                if i > upper_i:
                    i=i-1
                else:
                    right_pointer=1
                    down_pointer=0
                    left_j = left_j +1
                    j = j+1
            num=num+1
        return ans