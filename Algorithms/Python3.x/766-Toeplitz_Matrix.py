# Runtime: 84 ms, faster than 97.46% of Python3 online submissions for Toeplitz Matrix.
# Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Toeplitz Matrix.
class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        for row in range(len(matrix)):
            val = matrix[row][0]
            col = 0
            while row < len(matrix) and col < len(matrix[0]):
                if matrix[row][col] != val:
                    return False
                row += 1
                col += 1
        for col in range(len(matrix[0])):
            val = matrix[0][col]
            row = 0
            while row < len(matrix) and col < len(matrix[0]):
                if matrix[row][col] != val:
                    return False
                row += 1
                col += 1
        return True
