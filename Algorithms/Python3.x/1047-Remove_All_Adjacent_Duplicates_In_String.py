# stack
# Runtime: 68 ms, faster than 82.79% of Python3 online submissions for Remove All Adjacent Duplicates In String.
# Memory Usage: 12.9 MB, less than 100.00% of Python3 online submissions for Remove All Adjacent Duplicates In String.
class Solution:
    def removeDuplicates(self, S: str) -> str:
        stk = []
        for s in S:
            if stk and stk[-1] == s:
                stk.pop()
            else:
                stk.append(s)
        return "".join(stk)


# two pointer
# Runtime: 116 ms, faster than 19.71% of Python3 online submissions for Remove All Adjacent Duplicates In String.
# Memory Usage: 12.9 MB, less than 100.00% of Python3 online submissions for Remove All Adjacent Duplicates In String.
class Solution:
    def removeDuplicates(self, S: str) -> str:
        S = list(S)
        i, j = 0, 0
        while j < len(S):
            S[i] = S[j]
            if i > 0 and S[i - 1] == S[i]:
                i -= 2
            i += 1
            j += 1
        return "".join(S[:i])
