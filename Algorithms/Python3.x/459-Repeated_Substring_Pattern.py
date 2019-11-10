# Runtime: 24 ms, faster than 99.87% of Python3 online submissions for Repeated Substring Pattern.
# Memory Usage: 13 MB, less than 100.00% of Python3 online submissions for Repeated Substring Pattern.
class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        return s in (2 * s)[1:-1]
