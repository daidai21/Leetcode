# Runtime: 40 ms, faster than 82.48% of Python3 online submissions for Pancake Sorting.
# Memory Usage: 14 MB, less than 22.21% of Python3 online submissions for Pancake Sorting.
class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        res = []
        for x in range(len(arr), 1, -1):
            i = arr.index(x)
            res.extend([i + 1, x])
            arr = arr[:i:-1] + arr[:i]
        return res
