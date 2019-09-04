# Time Limit Exceeded
class Solution:
    def countDigitOne(self, n: int) -> int:
        count_one = 0
        for i in range(n + 1):
            count_one += list(str(i)).count('1')
        return count_one


# Runtime: 32 ms, faster than 89.11% of Python3 online submissions for Number of Digit One.
# Memory Usage: 13.8 MB, less than 100.00% of Python3 online submissions for Number of Digit One.
class Solution:
    def countDigitOne(self, n: int) -> int:
        ones, m = 0, 1
        while m <= n:
            ones += (n // m + 8) // 10 * m + (n // m % 10 == 1) * (n % m + 1)
            m *= 10
        return ones
