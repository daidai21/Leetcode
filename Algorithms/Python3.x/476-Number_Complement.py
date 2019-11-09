# Runtime: 28 ms, faster than 98.42% of Python3 online submissions for Number Complement.
# Memory Usage: 12.6 MB, less than 100.00% of Python3 online submissions for Number Complement.class Solution:
class Solution:
    def findComplement(self, num: int) -> int:
        num = [('1', '0')[int(x)] for x in bin(num)[2:]]
        return int(''.join(num), 2)
