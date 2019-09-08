# Runtime: 272 ms, faster than 50.00% of Python3 online submissions for Maximum of Absolute Value Expression.
# Memory Usage: 19.2 MB, less than 100.00% of Python3 online submissions for Maximum of Absolute Value Expression.
class Solution:
    def maxAbsValExpr(self, arr1: List[int], arr2: List[int]) -> int:
        res = 0
        for dx, dy in [(1, 1), 
                       (1, -1), 
                       (-1, 1), 
                       (-1, -1)]:
            max_val, min_val = 0, float("inf")
            for i in range(len(arr1)):
                max_val = max(max_val, dx * arr1[i] + dy * arr2[i] + i)
                min_val = min(min_val, dx * arr1[i] + dy * arr2[i] + i)
            res = max(res, max_val - min_val)
        return res
