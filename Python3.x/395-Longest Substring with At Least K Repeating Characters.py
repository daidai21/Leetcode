# Runtime: 40 ms, faster than 75.62% of Python3 online submissions for Longest Substring with At Least K Repeating Characters.
# Memory Usage: 13.4 MB, less than 17.98% of Python3 online submissions for Longest Substring with At Least K Repeating Characters.
class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        for c in set(s):
            if s.count(c) < k:
                return max(self.longestSubstring(t, k) for t in s.split(c))
        return len(s)


# Runtime: 36 ms, faster than 93.56% of Python3 online submissions for Longest Substring with At Least K Repeating Characters.
# Memory Usage: 13.1 MB, less than 88.83% of Python3 online submissions for Longest Substring with At Least K Repeating Characters.
class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        if len(s) < k:
            return 0
        c = min(set(s), key=s.count)
        if s.count(c) >= k:
            return len(s)
        return max(self.longestSubstring(t, k) for t in s.split(c))