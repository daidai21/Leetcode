# Runtime: 28 ms, faster than 99.43% of Python3 online submissions for Combination Sum III.
# Memory Usage: 13.7 MB, less than 11.11% of Python3 online submissions for Combination Sum III.
class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        self.res = []
        self.helper(k, n, 1, [])
        return self.res

    def helper(self, k, n, level, curr):
        if n < 0:
            return
        if n == 0 and k == 0:
            self.res.append(curr)
        for i in range(level, 10):
            self.helper(k - 1, n - i, i + 1, curr + [i])
