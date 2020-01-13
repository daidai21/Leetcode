# DP
# Runtime: 316 ms, faster than 88.48% of Python3 online submissions for Minimum Distance to Type a Word Using Two Fingers.
# Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Minimum Distance to Type a Word Using Two Fingers.
from functools import lru_cache


class Solution:
    def minimumDistance(self, word: str) -> int:
        @lru_cache(maxsize=None)
        def dis(n1, n2):
            if n1 == -1:
                return 0
            if n2 == -1:
                return 0
            return abs(n1 // 6 - n2 // 6) + abs(n1 % 6 - n2% 6)

        @lru_cache(maxsize=None)
        def to_num(ch):
            return ord(ch) - 65

        # key: (i,j) i is the position of the first finger, j is the positino of the second finger
        dp = {(to_num(word[0]), -1): 0}  # base case, -1 means the second finger is free
        for n in [to_num(ch) for ch in word[1:]]:
            new_dp = {}
            for (n1, n2), di in dp.items():
                new_dp[n, n2] = min(new_dp.get((n, n2), float("inf")), di + dis(n1, n))
                new_dp[n1, n] = min(new_dp.get((n1, n), float("inf")), di + dis(n2, n))
            dp = new_dp
        return min(dp.values())


print(Solution().minimumDistance("CAKE"))  # 3
print(Solution().minimumDistance("HAPPY"))  # 6
print(Solution().minimumDistance("NEW"))  # 3
print(Solution().minimumDistance("YEAR"))  # 7
