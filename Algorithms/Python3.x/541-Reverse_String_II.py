# Runtime: 32 ms, faster than 95.75% of Python3 online submissions for Reverse String II.
# Memory Usage: 12.9 MB, less than 100.00% of Python3 online submissions for Reverse String II.
class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        s = list(s)
        for start in range(0, len(s), 2 * k):
            end = min(start + k - 1, len(s) - 1)
            while start < end:
                s[start], s[end] = s[end], s[start]
                start += 1
                end -= 1
        return ''.join(s)


# direct
# Runtime: 32 ms, faster than 95.75% of Python3 online submissions for Reverse String II.
# Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Reverse String II.
class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        s = list(s)
        for i in range(0, len(s), 2 * k):
            s[i:i + k] = reversed(s[i:i + k])
        return ''.join(s)
