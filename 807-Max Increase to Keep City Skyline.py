class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        if grid == [] or grid == [[]]: return 0
        row_len, col_len, result = len(grid), len(grid[0]), 0
        max_row, max_col = [0] * row_len, [0] * col_len
        for row in range(row_len):  # search max row and col array
            for col in range(col_len):
                max_col[col] = max(max_col[col], grid[row][col])
                max_row[row] = max(max_row[row], grid[row][col])
        for row in range(row_len):  # computer add number
            for col in range(col_len):
                result += min(max_col[col], max_row[row]) - grid[row][col] if min(max_col[col], max_row[row]) - grid[row][col] else 0
        return result


# Runtime: 48 ms, faster than 80.67% of Python3 online submissions for Max Increase to Keep City Skyline.
# Memory Usage: 13 MB, less than 5.55% of Python3 online submissions for Max Increase to Keep City Skyline.
class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        row_max, col_max = [max(row) for row in grid], [max(col) for col in zip(*grid)]
        return sum(min(row_max[row], col_max[col]) - grid[row][col] for col in range(len(grid[0])) for row in range(len(grid)))
