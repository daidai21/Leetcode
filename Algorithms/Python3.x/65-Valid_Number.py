# Runtime: 44 ms, faster than 43.08% of Python3 online submissions for Valid Number.
# Memory Usage: 14.1 MB, less than 8.33% of Python3 online submissions for Valid Number.
class Solution:
    def isNumber(self, s: str) -> bool:
        try:
            float(s)
            return True
        except ValueError as err:
            return False
