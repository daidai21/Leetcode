# Runtime: 28 ms, faster than 99.19% of Python3 online submissions for Implement strStr().
# Memory Usage: 13.2 MB, less than 80.92% of Python3 online submissions for Implement strStr().
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        len_needle = len(needle)
        if len_needle == 0: return 0
        for start in range(0, len(haystack) - len_needle + 1):
            if haystack[start:start + len_needle] == needle: return start
        return -1
