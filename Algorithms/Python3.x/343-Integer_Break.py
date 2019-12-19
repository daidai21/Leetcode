# Runtime: 32 ms, faster than 78.35% of Python3 online submissions for Integer Break.
# Memory Usage: 12.9 MB, less than 100.00% of Python3 online submissions for Integer Break.
class Solution:
    def integerBreak(self, n: int) -> int:
        if n == 2:
            return 1
        if n == 3:
            return 2
        res = 1
        while n > 4:
            res *= 3
            n -= 3
        return res * n
