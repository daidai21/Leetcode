class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        col_sums = [0] * len(grid[0])
        row_sums = [0] * len(grid)
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col]:
                    col_sums[col] += 1
                    row_sums[row] += 1
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1:
                    if col_sums[col] > 1 or row_sums[row] > 1:
                        grid[row][col] = 2
        result = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                result += grid[row][col] == 2
        return result
