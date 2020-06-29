# Greedy
# Runtime: 32 ms, faster than 54.10% of Python3 online submissions for Valid Parenthesis String.
# Memory Usage: 13.7 MB, less than 84.78% of Python3 online submissions for Valid Parenthesis String.
class Solution:
    def checkValidString(self, s: str) -> bool:
        low, high = 0, 0
        for c in s:
            low  += 1 if c == "(" else -1
            high += 1 if c != ")" else -1
            if high < 0:
                break
            low = max(low, 0)
        return low == 0
