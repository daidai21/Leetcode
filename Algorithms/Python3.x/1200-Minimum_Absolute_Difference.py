# Runtime: 468 ms, faster than 17.07% of Python3 online submissions for Minimum Absolute Difference.
# Memory Usage: 28 MB, less than 100.00% of Python3 online submissions for Minimum Absolute Difference.
class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        result = []
        min_diff = float("inf")
        for i in range(1, len(arr)):
            if arr[i] - arr[i - 1] < min_diff:
                result = [[arr[i - 1], arr[i]]]
            elif arr[i] - arr[i - 1] == min_diff:
                result.append([arr[i - 1], arr[i]])
            min_diff = min(arr[i] - arr[i - 1], min_diff)
        return result
