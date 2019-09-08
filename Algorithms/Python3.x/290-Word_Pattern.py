# Runtime: 32 ms, faster than 89.51% of Python3 online submissions for Word Pattern.
# Memory Usage: 14 MB, less than 5.55% of Python3 online submissions for Word Pattern.
class Solution:
    def wordPattern(self, pattern: str, str: str) -> bool:
        return len(pattern) == len(str.split()) and all([i1 == i2 for i1, i2 in zip(map(pattern.find, pattern), map(str.split().index, str.split()))])
