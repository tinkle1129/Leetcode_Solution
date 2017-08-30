# - * - coding:utf8 - * - -
###########################################
# Author: Tinkle
# E-mail: shutingnjupt@gmail.com
# Name:   Range Sum Query 2D - Immutable.;y
# Creation Time: 2017/8/30
###########################################
'''
Example:
Given matrix = [
  [3, 0, 1, 4, 2],
  [5, 6, 3, 2, 1],
  [1, 2, 0, 1, 5],
  [4, 1, 0, 1, 7],
  [1, 0, 3, 0, 5]
]

sumRegion(2, 1, 4, 3) -> 8
sumRegion(1, 1, 2, 2) -> 11
sumRegion(1, 2, 2, 4) -> 12

'''


class NumMatrix(object):
    def __init__(self, matrix):
        """
        :type matrix: List[List[int]]
        """
        self.sumNum = [[matrix[i][j] for j in range(len(matrix[0]))] for i in range(len(matrix))]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if i>0:
                    self.sumNum[i][j] += self.sumNum[i-1][j]
                if j>0:
                    self.sumNum[i][j] += self.sumNum[i][j-1]
                if i>0 and j>0:
                    self.sumNum[i][j] -= self.sumNum[i-1][j-1]

    def sumRegion(self, row1, col1, row2, col2):
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        ret = self.sumNum[row2][col2]
        if row1>0:
            ret -= self.sumNum[row1-1][col2]
        if col1>0:
            ret -= self.sumNum[row2][col1-1]
        if row1>0 and col1>0:
            ret += self.sumNum[row1-1][col1-1]
        return ret



matrix = [
  [3, 0, 1, 4, 2],
  [5, 6, 3, 2, 1],
  [1, 2, 0, 1, 5],
  [4, 1, 0, 1, 7],
  [1, 0, 3, 0, 5]
]
obj = NumMatrix(matrix)
print obj.sumRegion(2, 1, 4, 3)
print obj.sumRegion(1, 1, 2, 2)
print obj.sumRegion(1, 2, 2, 4)

        # Your NumMatrix object will be instantiated and called as such:
        # obj = NumMatrix(matrix)
        # param_1 = obj.sumRegion(row1,col1,row2,col2)