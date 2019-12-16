# DP
# Runtime: 48 ms, faster than 87.23% of Python3 online submissions for Distinct Subsequences II.
# Memory Usage: 12.9 MB, less than 100.00% of Python3 online submissions for Distinct Subsequences II.
class Solution:
    def distinctSubseqII(self, S: str) -> int:
        dp = [1]
        last = {}
        for i, x in enumerate(S):
            dp.append(dp[-1] * 2)
            if x in last:
                dp[-1] -= dp[last[x]]
            last[x] = i
        return (dp[-1] - 1) % (10 ** 9 + 7)
