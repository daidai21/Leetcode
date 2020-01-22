# Runtime: 968 ms, faster than 10.93% of Python3 online submissions for Minimum Number of Taps to Open to Water a Garden.
# Memory Usage: 12.9 MB, less than 100.00% of Python3 online submissions for Minimum Number of Taps to Open to Water a Garden.
class Solution:
    def minTaps(self, n: int, ranges: List[int]) -> int:
        dp = [0] + [n + 2] * n
        for i, x in enumerate(ranges):
            for j in range(max(i - x + 1, 0), min(i + x, n) + 1):
                dp[j] = min(dp[j], dp[max(0, i - x)] + 1)
        return dp[n] if dp[n] < n + 2 else -1
