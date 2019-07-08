# Runtime: 56 ms, faster than 95.24% of Python3 online submissions for Roman to Integer.
# Memory Usage: 13.3 MB, less than 61.58% of Python3 online submissions for Roman to Integer.
class Solution:
    def romanToInt(self, s: str) -> int:
        if len(s) == 0: return 0
        dictory = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        s, res, i = list(s), 0, 0
        for i, val in enumerate(s):
            s[i] = dictory[s[i]]
        len_s = len(s)
        for i, _ in enumerate(s[:-1]):
                res = res - s[i] if s[i] < s[i + 1] else res + s[i]
        res += s[-1]
        return res
