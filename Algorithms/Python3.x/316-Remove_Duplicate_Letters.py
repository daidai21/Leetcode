# Runtime: 56 ms, faster than 27.79% of Python3 online submissions for Remove Duplicate Letters.
# Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Remove Duplicate Letters.
class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        for ch in sorted(set(s)):
            suffix = s[s.index(ch):]
            if set(suffix) == set(s):
                return ch + self.removeDuplicateLetters(suffix.replace(ch, ""))
        return ""
