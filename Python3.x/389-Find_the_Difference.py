# Runtime: 608 ms, faster than 6.58% of Python3 online submissions for Find the Difference.
# Memory Usage: 13.8 MB, less than 10.00% of Python3 online submissions for Find the Difference.
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        s, t = list(s), list(t)
        for i in range(len(s)):
            for j in range(len(t)):
                if s[i] == t[j]:
                    t[j] = None
                    break
        for j in t:
            if j is not None:
                return j
