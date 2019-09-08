# Runtime: 68 ms, faster than 98.88% of Python3 online submissions for Search a 2D Matrix.
# Memory Usage: 15.7 MB, less than 5.01% of Python3 online submissions for Search a 2D Matrix.
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for line in matrix:
            for val in line:
                if val == target:
                    return True
        return False


# Runtime: 76 ms, faster than 83.52% of Python3 online submissions for Search a 2D Matrix.
# Memory Usage: 15.7 MB, less than 5.01% of Python3 online submissions for Search a 2D Matrix.
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return False
        row, col = len(matrix) - 1, 0
        while matrix[row][col] > target and row > 0:
            row -= 1
        while matrix[row][col] < target and col < len(matrix[0]) - 1:
            col += 1
        return matrix[row][col] == target
