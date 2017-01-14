'''
class Solution(object):
	def rotate(self, matrix):
		n = len(matrix)

		a[j][n-1-i]=a[i][j]

		tmp = [[matrix[n-1-j][i] for j in range(n)] for i in range(n)]
		matrix = [[tmp[i][j] for j in range(n)] for i in range(n)]
'''

class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        size = len(matrix)
        for i in range(size):
            for j in range(i + 1,size):
                matrix[i][j],matrix[j][i] = matrix[j][i],matrix[i][j]
        for i in range(size):
            matrix[i].reverse()