# Runtime: 232 ms, faster than 90.32% of Python3 online submissions for Longest Increasing Path in a Matrix.
# Memory Usage: 13.5 MB, less than 88.86% of Python3 online submissions for Longest Increasing Path in a Matrix.
class Solution:
    def longestIncreasingPath(self, matrix):
        if not matrix: return 0
        len_row, len_col = len(matrix), len(matrix[0])
        dp = [[0] * len_col for _ in range(len_row)]
        return max(self.dfs(matrix, dp, row, col, len_row, len_col) for row in range(len_row) for col in range(len_col))

    def dfs(self, matrix, dp, row, col, len_row, len_col):
        if not dp[row][col]:
            val = matrix[row][col]
            dp[row][col] = 1 + max(
                self.dfs(matrix, dp, row - 1, col, len_row, len_col) if row > 0 and val > matrix[row - 1][col] else 0,
                self.dfs(matrix, dp, row + 1, col, len_row, len_col) if row < len_row - 1 and val > matrix[row + 1][col] else 0,
                self.dfs(matrix, dp, row, col - 1, len_row, len_col) if col > 0 and val > matrix[row][col - 1] else 0,
                self.dfs(matrix, dp, row, col + 1, len_row, len_col) if col < len_col - 1 and val > matrix[row][col + 1] else 0
            )
        return dp[row][col]