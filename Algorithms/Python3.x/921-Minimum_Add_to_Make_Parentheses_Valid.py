# Runtime: 32 ms, faster than 94.89% of Python3 online submissions for Minimum Add to Make Parentheses Valid.
# Memory Usage: 13.8 MB, less than 8.33% of Python3 online submissions for Minimum Add to Make Parentheses Valid.
class Solution:
    def minAddToMakeValid(self, S: str) -> int:
        left_brackets = 0
        min_add = 0
        for s in S:
            if s == '(':
                left_brackets += 1
            elif s == ')':
                left_brackets -= 1
            if left_brackets < 0:
                min_add += 0 - left_brackets
                left_brackets = 0
        return min_add + left_brackets
