# Runtime: 0 ms, faster than 100.00% of Python3 online submissions for Unique Paths III.
# Memory Usage: 13.9 MB, less than 7.69% of Python3 online submissions for Unique Paths III.
# dfs + backtracking
class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        self.result = 0
        end, non_empty_count = (), 1
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1:
                    x, y = row, col
                elif grid[row][col] == 2:
                    end = (row, col)
                elif grid[row][col] == 0:
                    non_empty_count += 1
        len_row, len_col = len(grid), len(grid[0])
        def dfs(i, j, non_empty_count):
            if 0 <= i < len_row and 0 <= j < len_col and grid[i][j] >= 0:
                if (i, j) == end:
                    self.result += non_empty_count == 0
                else:
                    grid[i][j] = -2
                    for x, y in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
                        dfs(x, y, non_empty_count - 1)
                    grid[i][j] = 0

        dfs(x, y, non_empty_count)
        return self.result
