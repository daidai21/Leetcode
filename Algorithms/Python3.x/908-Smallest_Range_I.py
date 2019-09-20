# Runtime: 140 ms, faster than 37.46% of Python3 online submissions for Smallest Range I.
# Memory Usage: 14.9 MB, less than 11.11% of Python3 online submissions for Smallest Range I.
class Solution:
    def smallestRangeI(self, A: List[int], K: int) -> int:
        return max(max(A) - min(A) - 2 * K, 0)
