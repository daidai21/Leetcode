# Runtime: 36 ms, faster than 83.47% of Python3 online submissions for Sum of Two Integers.
# Memory Usage: 13.3 MB, less than 8.57% of Python3 online submissions for Sum of Two Integers.
class Solution:
    def getSum(self, a: int, b: int) -> int:
        MAX, MIN, mask = 0x7FFFFFFF, 0x80000000, 0xFFFFFFFF
        while b != 0:
            a, b = (a ^ b) & mask, ((a & b) << 1) & mask
        return a if a <= MAX else ~(a ^ mask)  # ～是按位取反
