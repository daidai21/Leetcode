# Runtime: 1412 ms, faster than 6.71% of Python3 online submissions for Arranging Coins.
# Memory Usage: 13.9 MB, less than 5.00% of Python3 online submissions for Arranging Coins.
class Solution:
    def arrangeCoins(self, n: int) -> int:
        cnt = 0
        i = 1
        while n - i >= 0:
            cnt += 1
            n -= i
            i += 1
        return cnt


# Runtime: 56 ms, faster than 47.73% of Python3 online submissions for Arranging Coins.
# Memory Usage: 14 MB, less than 5.00% of Python3 online submissions for Arranging Coins.
# math
class Solution:
    def arrangeCoins(self, n: int) -> int:
        return int((2 * n + 0.25) ** 0.5 - 0.5)
