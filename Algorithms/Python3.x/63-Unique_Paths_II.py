class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if not obstacleGrid or obstacleGrid == []:
            return 0
        len_row, len_col = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[0] * len_col for _ in range(len_row)]
        dp[0][0] = 1 if obstacleGrid[0][0] == 0 else 0
        for row in range(1, len_row):
            dp[row][0] = dp[row - 1][0] if obstacleGrid[row][0] == 0 else 0
        for col in range(1, len_col):
            dp[0][col] = dp[0][col - 1] if obstacleGrid[0][col] == 0 else 0
        for row in range(1, len_row):
            for col in range(1, len_col):
                dp[row][col] = dp[row - 1][col] + dp[row][col - 1] if obstacleGrid[row][col] == 0 else 0
        return dp[-1][-1]
