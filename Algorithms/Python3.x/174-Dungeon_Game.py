# DP
# Runtime: 72 ms, faster than 90.53% of Python3 online submissions for Dungeon Game.
# Memory Usage: 13.6 MB, less than 100.00% of Python3 online submissions for Dungeon Game.
class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        dp = [[float("inf")] * (len(dungeon[0]) + 1) for _ in range(len(dungeon) + 1)]
        dp[-1][-2] = 1
        dp[-2][-1] = 1
        for row in range(len(dungeon) - 1, -1, -1):
            for col in range(len(dungeon[0]) - 1, -1, -1):
                need = min(dp[row + 1][col], dp[row][col + 1]) - dungeon[row][col]
                dp[row][col] = max(1, need)
        return dp[0][0]
