# Runtime: 124 ms, faster than 82.13% of Python3 online submissions for Range Sum Query 2D - Immutable.
# Memory Usage: 16.7 MB, less than 16.67% of Python3 online submissions for Range Sum Query 2D - Immutable.
class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        if not matrix:
            return
        len_row, len_col = len(matrix), len(matrix[0])
        self.mat = [[0] * (len_col + 1) for _ in range(len_row + 1)]
        for row in range(1, len_row + 1):
            for col in range(1, len_col + 1):
                self.mat[row][col] = matrix[row - 1][col - 1] + self.mat[row][col - 1] + self.mat[row - 1][col] - self.mat[row - 1][col - 1]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self.mat[row2 + 1][col2 + 1] - self.mat[row1][col2 + 1] - self.mat[row2 + 1][col1] + self.mat[row1][col1]


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
