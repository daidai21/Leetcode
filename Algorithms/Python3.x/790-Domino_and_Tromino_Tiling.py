# Runtime: 24 ms, faster than 100.00% of Python3 online submissions for Domino and Tromino Tiling.
# Memory Usage: 12.6 MB, less than 100.00% of Python3 online submissions for Domino and Tromino Tiling.
# finding rules && DP
# Space: O(n)
# Time: O(n)
class Solution:
    def numTilings(self, N: int) -> int:
        MOD = 10 ** 9 + 7
        dp = [1, 1, 2, 5]
        if N < 4:
            return dp[N]
        for _ in range(N - 3):
            dp.append((2 * dp[-1] + dp[-3]) % MOD)
        return dp[-1]


# finding rules && DP
# Space: O(1)
# Time: O(n)
# Runtime: 28 ms, faster than 97.28% of Python3 online submissions for Domino and Tromino Tiling.
# Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for Domino and Tromino Tiling.
class Solution:
    def numTilings(self, N: int) -> int:
        MOD = 10 ** 9 + 7
        a, b, c = 0, 1, 1
        for _ in range(N - 1):
            a, b, c = b, c, (2 * c + a) % MOD
        return c
