# Runtime: 36 ms, faster than 77.16% of Python3 online submissions for Power of Two.
# Memory Usage: 13.2 MB, less than 57.80% of Python3 online submissions for Power of Two.
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        tmp = 1
        while tmp <= n:
            if tmp == n:
                return True
            tmp *= 2
        return False
