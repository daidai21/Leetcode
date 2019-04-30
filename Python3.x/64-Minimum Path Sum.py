# dp
# space: 1
class Solution:
    def minPathSum(self, grid: 'List[List[int]]') -> 'int':
        row, col = len(grid), len(grid[0])
        for i in range(1, col): grid[0][i] += grid[0][i - 1]
        for i in range(1, row): grid[i][0] += grid[i - 1][0]
        for r in range(1, row):
            for c in range(1, col):
                grid[r][c] = min(grid[r-1][c], grid[r][c-1]) + grid[r][c]
        return grid[row-1][col-1]


'''
dp直接在输入的grid矩阵中更新
'''


# dp
# space: row * col
class Solution:
    def minPathSum(self, grid: 'List[List[int]]') -> 'int':
        dp = [[0 for _ in range(len(grid[0]))] for _ in range(len(grid))]
        dp[0][0] = grid[0][0]
        for i in range(1, len(grid)): dp[i][0] = dp[i - 1][0] + grid[i][0]
        for i in range(1, len(grid[0])): dp[0][i] = dp[0][i - 1] + grid[0][i]
        for row in range(1, len(grid)):
            for col in range(1, len(grid[0])):
                dp[row][col] = min(dp[row][col - 1], dp[row - 1][col]) + grid[row][col]
        return dp[-1][-1]
