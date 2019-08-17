# Runtime: 36 ms, faster than 81.85% of Python3 online submissions for Ugly Number.
# Memory Usage: 14 MB, less than 6.67% of Python3 online submissions for Ugly Number.
class Solution:
    def isUgly(self, num: int) -> bool:
        if num == 0:
            return False
        while num % 2 == 0:
            num /= 2
        while num % 3 == 0:
            num /= 3
        while num % 5 == 0:
            num /= 5
        return num == 1
