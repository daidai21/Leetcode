# Runtime: 68 ms, faster than 77.75% of Python3 online submissions for Range Addition II.
# Memory Usage: 14.5 MB, less than 33.33% of Python3 online submissions for Range Addition II.
class Solution:
    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
        for x, y in ops:
            m = min(m, x)
            n = min(n, y)
        return m * n


# Runtime: 72 ms, faster than 52.60% of Python3 online submissions for Range Addition II.
# Memory Usage: 14.6 MB, less than 33.33% of Python3 online submissions for Range Addition II.
class Solution:
    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
        return min([m] + [x for x, _ in ops]) * min([n] + [y for _, y in ops])
