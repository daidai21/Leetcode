# DP
# Runtime: 348 ms, faster than 84.10% of Python3 online submissions for Binary Trees With Factors.
# Memory Usage: 12.9 MB, less than 100.00% of Python3 online submissions for Binary Trees With Factors.
class Solution:
    def numFactoredBinaryTrees(self, A: List[int]) -> int:
        dp = {}
        for a in sorted(A):
            dp[a] = 1
            for b in dp:
                if a % b == 0:
                    dp[a] += dp[b] * dp.get(a / b, 0)
        return sum(dp.values()) % (10 ** 9 + 7)
