# Runtime: 52 ms, faster than 96.52% of Python3 online submissions for Swap For Longest Repeated Character Substring.
# Memory Usage: 15.9 MB, less than 24.74% of Python3 online submissions for Swap For Longest Repeated Character Substring.
class Solution:
    def maxRepOpt1(self, text: str) -> int:
        A = [[c, len(list(g))] for c, g in itertools.groupby(text)]
        C = collections.Counter(text)
        res = max(min(k + 1, C[c]) for c, k in A)
        for i in range(1, len(A) - 1):
            if A[i - 1][0] == A[i + 1][0] and A[i][1] == 1:
                res = max(res, min(A[i - 1][1] + A[i + 1][1] + 1, C[A[i + 1][0]]))
        return res
