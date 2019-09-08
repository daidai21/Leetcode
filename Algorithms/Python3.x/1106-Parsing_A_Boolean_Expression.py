# Runtime: 64 ms, faster than 68.82% of Python3 online submissions for Parsing A Boolean Expression.
# Memory Usage: 13.2 MB, less than 100.00% of Python3 online submissions for Parsing A Boolean Expression.
class Solution:
    def parseBoolExpr(self, expression: str) -> bool:
        self.exp = expression
        return self.func(0)[0]

    def func(self, i):
        if self.exp[i] in ['t', 'f']:  # translate char
            return True if self.exp[i] == 't' else False, i + 1
        opt = self.exp[i]
        i, stack = i + 2, []
        while self.exp[i] != ')':
            if self.exp[i] == ',':
                i += 1
                continue
            res, i = self.func(i)
            stack.append(res)
        if opt == '&':
            return all(stack), i + 1
        elif opt == '|':
            return any(stack), i + 1
        elif opt == '!':
            return not stack[0], i + 1
