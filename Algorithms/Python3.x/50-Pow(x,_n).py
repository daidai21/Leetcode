# space: log(n)
# Runtime: 32 ms, faster than 93.92% of Python3 online submissions for Pow(x, n).
# Memory Usage: 13.1 MB, less than 88.93% of Python3 online submissions for Pow(x, n).
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0: return 1
        if n < 0: return 1.0 / self.myPow(x, -n)
        half = self.myPow(x, n // 2)
        if n % 2 == 0:
            return half * half
        else:
            return half * half * x
