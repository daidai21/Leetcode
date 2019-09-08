# Runtime: 36 ms, faster than 63.24% of Python3 online submissions for Number of Segments in a String.
# Memory Usage: 14 MB, less than 6.67% of Python3 online submissions for Number of Segments in a String.
class Solution:
    def countSegments(self, s: str) -> int:
        return len(s.split())
