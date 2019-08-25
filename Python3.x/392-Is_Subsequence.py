# Runtime: 180 ms, faster than 47.97% of Python3 online submissions for Is Subsequence.
# Memory Usage: 26.5 MB, less than 26.67% of Python3 online submissions for Is Subsequence.
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        s, t = list(s), list(t)
        idx = 0
        for i in range(len(s)):
            if s[i] in t[idx:]:
                idx = t.index(s[i], idx)
                t[idx] = None
                idx += 1
            else:
                return False
        return True
