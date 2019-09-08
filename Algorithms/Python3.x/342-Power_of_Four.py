# Runtime: 40 ms, faster than 56.56% of Python3 online submissions for Power of Four.
# Memory Usage: 14 MB, less than 8.70% of Python3 online submissions for Power of Four.
class Solution:
    def isPowerOfFour(self, num: int) -> bool:
        return num & (num - 1) == 0 and (num - 1) % 3 == 0
