# Runtime: 52 ms, faster than 53.33% of Python3 online submissions for Shortest Distance to a Character.
# Memory Usage: 14 MB, less than 7.69% of Python3 online submissions for Shortest Distance to a Character.
class Solution:
    def shortestToChar(self, S: str, C: str) -> List[int]:
        dp = [float("inf")] * len(S)
        for i, s in enumerate(S):
            if s == C:
                dp[i] = 0
        for i in range(1, len(S)):
            if dp[i - 1] is not None:
                dp[i] = min(dp[i], dp[i - 1] + 1)
        for i in range(len(S) - 2, -1, -1):
            if dp[i + 1] is not None:
                dp[i] = min(dp[i], dp[i + 1] + 1)
        return dp
