# Runtime: 708 ms, faster than 59.42% of Python3 online submissions for Guess Number Higher or Lower II.
# Memory Usage: 14.3 MB, less than 100.00% of Python3 online submissions for Guess Number Higher or Lower II.
# minimax dp
class Solution:
    def getMoneyAmount(self, n: int) -> int:
        dp = [[0] * (n + 1) for _ in range(n + 1)]
        for low in range(n, 0, -1):
            for high in range(low + 1, n + 1):
                tmp = float("inf")
                for x in range(low, high):
                    tmp = min(tmp, x + max(dp[low][x - 1], dp[x + 1][high]))
                dp[low][high] = tmp
        return dp[1][n]
