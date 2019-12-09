# Runtime: 20 ms, faster than 99.01% of Python3 online submissions for N-th Tribonacci Number.
# Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for N-th Tribonacci Number.
class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        elif n < 2:
            return 1
        else:
            t0, t1, t2 = 0, 1, 1
            for _ in range(n - 2):
                t0, t1, t2 = t1, t2, t0 + t1 + t2
            return t2
