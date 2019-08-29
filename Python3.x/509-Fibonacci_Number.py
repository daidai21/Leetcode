# Runtime: 40 ms, faster than 41.89% of Python3 online submissions for Fibonacci Number.
# Memory Usage: 14 MB, less than 5.80% of Python3 online submissions for Fibonacci Number.
class Solution:
    def fib(self, N: int) -> int:
        if N < 2:
            return N
        else:
            pre, cur = 0, 1
            for _ in range(N - 1):
                pre, cur = cur, pre + cur
            return cur
