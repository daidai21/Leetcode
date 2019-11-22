# Runtime: 740 ms, faster than 68.59% of Python3 online submissions for 01 Matrix.
# Memory Usage: 14.9 MB, less than 75.00% of Python3 online submissions for 01 Matrix.
# BFS
class Solution:
    def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        len_row, len_col, queue = len(matrix), len(matrix[0]), []
        for row in range(len_row):
            for col in range(len_col):
                if matrix[row][col] != 0:
                    matrix[row][col] = float("inf")
                else:
                    queue.append((row, col))
        for i, j in queue:
            for r, c in ((i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)):
                z = matrix[i][j] + 1
                if 0 <= r < len_row and 0 <= c < len_col and matrix[r][c] > z:
                    matrix[r][c] = z
                    queue.append((r, c))
        return matrix


# Runtime: 864 ms, faster than 38.62% of Python3 online submissions for 01 Matrix.
# Memory Usage: 14.8 MB, less than 83.33% of Python3 online submissions for 01 Matrix.
# BFS
class Solution:
    def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        len_row, len_col, queue = len(matrix), len(matrix[0]), []
        for row in range(len_row):
            for col in range(len_col):
                if matrix[row][col] != 0:
                    matrix[row][col] = float("inf")
                else:
                    queue.append((row, col))
        while queue:
            i, j = queue.pop(0)
            for r, c in ((i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)):
                z = matrix[i][j] + 1
                if 0 <= r < len_row and 0 <= c < len_col and matrix[r][c] > z:
                    matrix[r][c] = z
                    queue.append((r, c))
        return matrix
