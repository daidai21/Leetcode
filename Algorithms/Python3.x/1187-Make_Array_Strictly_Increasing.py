# dp
# Runtime: 816 ms, faster than 100.00% of Python3 online submissions for Make Array Strictly Increasing.
# Memory Usage: 14 MB, less than 100.00% of Python3 online submissions for Make Array Strictly Increasing.
class Solution:
    def makeArrayIncreasing(self, arr1: List[int], arr2: List[int]) -> int:
        dp = {-1: 0}
        arr2.sort()
        for i in arr1:
            tmp = collections.defaultdict(lambda: float('inf'))
            for key in dp:
                if i > key:
                    tmp[i] = min(tmp[i], dp[key])
                loc = bisect.bisect_right(arr2, key)
                if loc < len(arr2):
                    tmp[arr2[loc]] = min(tmp[arr2[loc]], dp[key] + 1)
            dp = tmp
        if dp:
            return min(dp.values())
        return -1


"""
The key of dp is current max value (that is item of sorted array end)
The value of dp is min operators
"""
