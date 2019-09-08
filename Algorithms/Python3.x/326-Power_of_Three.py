# Runtime: 52 ms, faster than 98.67% of Python online submissions for Power of Three.
# Memory Usage: 11.8 MB, less than 16.55% of Python online submissions for Power of Three.
class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n < 1: return False
        while n % 3 == 0:
            n /= 3
        return n == 1
