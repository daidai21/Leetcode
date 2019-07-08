# one line
# Runtime: 336 ms, faster than 30.37% of Python3 online submissions for Sum of Square Numbers.
# Memory Usage: 13.5 MB, less than 17.34% of Python3 online submissions for Sum of Square Numbers.
class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        return any(int((c - i * i) ** 0.5) ** 2 == (c - i * i) for i in range(int(c ** 0.5) + 1))


# 暴力 超时
class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        i, j = 0, int(c + 1 / 2)
        while True:
            tmp = i * i + j * j
            if i > j: return False
            if tmp > c: j -= 1
            elif tmp < c: i += 1
            else: return True


# using library of math
# Runtime: 200 ms, faster than 74.86% of Python3 online submissions for Sum of Square Numbers.
# Memory Usage: 13.4 MB, less than 25.08% of Python3 online submissions for Sum of Square Numbers.
import math


class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        for i in range(0, int(math.sqrt(c) + 1)):
            j = math.sqrt(c - i * i)
            if j == int(j): return True
        return False


# 超时
class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        for i in range(0, int(math.sqrt(c) + 1)):
            j = c - i * i
            if self.binary_search(0, j, j): return True
        return False

    def binary_search(self, start, end, n):
        if start > end: return False
        mid = int(start + (end - start) / 2)

        if mid * mid == n: return True
        if mid * mid > n: return self.binary_search(start, mid - 1, n)
        else: return self.binary_search(mid + 1, end, n)


# using set()
# Runtime: 288 ms, faster than 45.05% of Python3 online submissions for Sum of Square Numbers.
# Memory Usage: 17 MB, less than 10.68% of Python3 online submissions for Sum of Square Numbers.
class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        sq = set()
        for i in range(int(math.sqrt(c)) + 1):
            sq.add(i ** 2)
        for n in sq:
            if c - n in sq: return True
        return False
