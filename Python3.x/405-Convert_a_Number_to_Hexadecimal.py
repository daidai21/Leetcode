# Runtime: 36 ms, faster than 69.49% of Python3 online submissions for Convert a Number to Hexadecimal.
# Memory Usage: 13.8 MB, less than 50.00% of Python3 online submissions for Convert a Number to Hexadecimal.
class Solution:
    def toHex(self, num: int) -> str:
        return hex(2 ** 32 + num)[2:] if num < 0 else hex(num)[2:]
