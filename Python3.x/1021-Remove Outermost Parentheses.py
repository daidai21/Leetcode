# Runtime: 40 ms, faster than 89.47% of Python3 online submissions for Remove Outermost Parentheses.
# Memory Usage: 14 MB, less than 5.10% of Python3 online submissions for Remove Outermost Parentheses.
class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        res, opened = "", 0
        for s in S:
            if s == '(' and opened > 0:
                res += s
            if s == ')' and opened > 1:
                res += s
            opened += 1 if s == '(' else -1
        return res
