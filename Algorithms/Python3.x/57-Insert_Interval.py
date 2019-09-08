# Runtime: 96 ms, faster than 53.41% of Python3 online submissions for Insert Interval.
# Memory Usage: 17.2 MB, less than 8.00% of Python3 online submissions for Insert Interval.
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not intervals:
            return [newInterval]
        # find insert index
        idx = 0
        while idx < len(intervals) and intervals[idx][0] <= newInterval[0]:
            idx += 1
        while idx < len(intervals) and intervals[idx][0] == newInterval[0] and intervals[idx][1] < newInterval[1]:
            idx += 1
        intervals.insert(idx, newInterval)
        res = []
        for i in range(len(intervals)):
            if not res or res[-1][1] < intervals[i][0]:
                res.append(intervals[i])
            else:
                if res[-1][1] >= intervals[i][0]:
                    res[-1][1] = max(intervals[i][1], res[-1][1])
        return res
