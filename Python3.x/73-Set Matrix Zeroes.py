# logistic
# Runtime: 96 ms, faster than 79.75% of Python3 online submissions for Set Matrix Zeroes.
# Memory Usage: 13.4 MB, less than 77.35% of Python3 online submissions for Set Matrix Zeroes.
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        zero_idx = []
        len_row, len_col = len(matrix), len(matrix[0])
        for i, line in enumerate(matrix):
            for j, val in enumerate(line):
                if val == 0: zero_idx.append((i, j))
        for _, (i, j) in enumerate(zero_idx):
            for z in range(len_col):
                matrix[i][z] = 0
            for z in range(len_row):
                matrix[z][j] = 0
