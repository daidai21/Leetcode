# Runtime: 48 ms, faster than 15.47% of Python3 online submissions for Height Checker.
# Memory Usage: 13.7 MB, less than 100.00% of Python3 online submissions for Height Checker.
class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        return len(heights) - sum([h1 == h2 for h1, h2 in zip(sorted(heights), heights)])
