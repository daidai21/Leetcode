# dp
# Runtime: 88 ms, faster than 74.62% of Python3 online submissions for Maximal Square.
# Memory Usage: 13.2 MB, less than 62.79% of Python3 online submissions for Maximal Square.
class Solution:
    def maximalSquare(self, matrix: 'List[List[str]]') -> 'int':
        if not matrix: return 0
        row_len, col_len = len(matrix), len(matrix[0])
        dp = [[0 if matrix[row][col] == '0' else 1 for col in range(col_len)] for row in range(row_len)]
        for row in range(1, row_len):
            for col in range(1, col_len):
                if matrix[row][col] == '1': dp[row][col] = min(dp[row - 1][col], dp[row][col - 1], dp[row - 1][col - 1]) + 1
                else: dp[row][col] = 0
        result = max(max(row) for row in dp)
        return result ** 2


'''
dp矩阵更新后存储
    以这个点为正方形右下角时，正方形最大的满足条件的边长
'''
