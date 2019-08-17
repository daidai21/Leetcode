# Time Limit Exceeded
class Solution:
    def canWinNim(self, n: int) -> bool:
        dp = [None, True, True, True]
        if n < 4:
            return dp[n]
        for i in range(4, n + 1):
            if dp[i - 1] and dp[i - 2] and dp[i - 3]:
                dp.append(False)
            else:
                dp.append(True)
        return dp[n]


# Runtime: 36 ms, faster than 62.47% of Python3 online submissions for Nim Game.
# Memory Usage: 13.8 MB, less than 14.29% of Python3 online submissions for Nim Game.
class Solution:
    def canWinNim(self, n: int) -> bool:
        return n % 4 != 0


class Solution:
    def canWinNim(self, n: int) -> bool:
        return n & 3 != 0
