# 标准dp问题
class Solution:
    def uniquePaths(self, m: 'int', n: 'int') -> 'int':
        dp = [[0 for _ in range(m)] for _ in range(n)]  # 这里m*n对应的是arr的(m - 1) * (n - 1)
        for i in range(m):
            dp[0][i] = 1
        for i in range(n):
            dp[i][0] = 1
        for row in range(1, n):
            for col in range(1, m):
                dp[row][col] = dp[row - 1][col] + dp[row][col - 1]
        return dp[n - 1][m - 1]

