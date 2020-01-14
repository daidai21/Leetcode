# Memory Limit Exceeded
class Solution:
    def findNthDigit(self, n: int) -> int:
        s = "".join([str(i) for i in range(1, n + 1)])
        return int(s[n - 1])


# math
# Runtime: 24 ms, faster than 85.57% of Python3 online submissions for Nth Digit.
# Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for Nth Digit.
class Solution:
    def findNthDigit(self, n: int) -> int:
        n -= 1
        for digits in range(1, 11):
            first = 10 ** (digits - 1)
            if n < 9 * first * digits:
                return int(str(first + n / digits)[n % digits])
            n -= 9 * first * digits


print(Solution().findNthDigit(3))
print(Solution().findNthDigit(11))
print(Solution().findNthDigit(1000001))
