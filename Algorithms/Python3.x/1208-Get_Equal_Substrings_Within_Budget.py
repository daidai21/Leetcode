# standard sliding window problem
# Runtime: 72 ms, faster than 100.00% of Python3 online submissions for Get Equal Substrings Within Budget.
# Memory Usage: 14.5 MB, less than 100.00% of Python3 online submissions for Get Equal Substrings Within Budget.
class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        i = 0
        for j in range(len(s)):
            maxCost -= abs(ord(s[j]) - ord(t[j]))
            if maxCost < 0:
                maxCost += abs(ord(s[i]) - ord(t[i]))
                i += 1
        return j - i + 1
