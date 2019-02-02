class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        for i in range(n):
            for j in range(i + 1, n):
                if i < j: matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        print(matrix)
        for row in matrix: row.reverse()


'''
原始：[[1,2,3], [4,5,6], [7,8,9]]
矩阵转置后：[[1, 4, 7], [2, 5, 8], [3, 6, 9]]
行转置后：[[7, 4, 1], [8, 5, 2], [9, 6, 3]]
'''
