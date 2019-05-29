# using the sqrt function of math library
# Runtime: 32 ms, faster than 95.65% of Python3 online submissions for Valid Perfect Square.
# Memory Usage: 12.8 MB, less than 94.93% of Python3 online submissions for Valid Perfect Square.
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        return True if int(math.sqrt(num)) ** 2 == num else False


# binary search
# Runtime: 32 ms, faster than 95.65% of Python3 online submissions for Valid Perfect Square.
# Memory Usage: 13.2 MB, less than 50.92% of Python3 online submissions for Valid Perfect Square.
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        return True if self.binary_search(0, num, num) else False

    def binary_search(self, start, end, n):
        if start > end: return False
        mid = int(start + (end - start) / 2)
        if mid * mid == n: return True
        return self.binary_search(start, mid - 1, n) if mid * mid > n else self.binary_search(mid + 1, end, n)


# 超时
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        i = num
        while True:
            if i * i == num: return True
            if i * i < num: return False
            if i * i > num: i -= 1


# Runtime: 32 ms, faster than 95.65% of Python3 online submissions for Valid Perfect Square.
# Memory Usage: 13.1 MB, less than 64.29% of Python3 online submissions for Valid Perfect Square.
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        return (int(num ** 0.5)) ** 2 == num

