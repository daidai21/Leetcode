# Runtime: 56 ms, faster than 95.78% of Python3 online submissions for Bitwise AND of Numbers Range.
# Memory Usage: 13.8 MB, less than 100.00% of Python3 online submissions for Bitwise AND of Numbers Range.
class Solution:
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        temp = 2147483647  # 2 ** 31 - 1
        while (temp & m) != (temp & n):
            temp = temp << 1
        return temp & m


# Runtime: 76 ms, faster than 34.94% of Python3 online submissions for Bitwise AND of Numbers Range.
# Memory Usage: 13.8 MB, less than 100.00% of Python3 online submissions for Bitwise AND of Numbers Range.
class Solution:
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        step = 0
        while m != n:
            m >>= 1
            n >>= 1
            step += 1
        return m << step
