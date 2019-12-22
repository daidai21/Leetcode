# Runtime: 72 ms, faster than 87.72% of Python3 online submissions for Minimum Time Difference.
# Memory Usage: 15.6 MB, less than 100.00% of Python3 online submissions for Minimum Time Difference.
class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        val_lst = []
        for time in timePoints:
            val_lst.append(int(time[:2]) * 60 + int(time[3:]))
        val_lst.sort()
        min_diff = min(float("inf"), (val_lst[0] - val_lst[-1]) % (24 * 60))
        for idx in range(1, len(val_lst)):
            min_diff = min(min_diff, (val_lst[idx] - val_lst[idx - 1]) % (24 * 60))
        return min_diff
