from typing import List


# Runtime: 64 ms, faster than 33.95% of Python3 online submissions for Letter Case Permutation.
# Memory Usage: 13.8 MB, less than 20.00% of Python3 online submissions for Letter Case Permutation.
class Solution:
    def letterCasePermutation(self, S: str) -> List[str]:
        def DFS(cur, idx):
            if idx >= len(cur):
                res.append(cur)
                return 
            if not cur[idx].isdigit():
                DFS(cur[:idx] + cur[idx].upper() + cur[idx + 1:], idx + 1)  # index char to upper
                DFS(cur[:idx] + cur[idx].lower() + cur[idx + 1:], idx + 1)  # index char to lower
            else:
                DFS(cur, idx + 1)  # index char to lower

        res = []
        DFS(S.lower(), 0)
        return res
