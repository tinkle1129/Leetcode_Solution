# - * - coding:utf8 - * - -
###########################################
# Author: Tinkle
# E-mail: shutingnupt@gmail.com
# Name:  Spiral Matrix.py
# Creation Time: 2017/7/5
###########################################
'''
Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.

For example,
Given the following matrix:

[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
You should return [1,2,3,6,9,8,7,4,5].
'''
class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        m=len(matrix)
        ans=[]
        if m==0:
            return ans
        n=len(matrix[0])
        #ans = [[0 for i in range(n)] for j in range(n)]
        #print ans
        upper_i =0;lower_i=m-1;left_j=0;right_j=n-1
        num=1
        i=0;j=0
        right_pointer=1
        down_pointer=0
        while(num<=m*n):
            ans.append(matrix[i][j])
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