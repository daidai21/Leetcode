# Runtime: 32 ms, faster than 83.45% of Python3 online submissions for Day of the Year.
# Memory Usage: 12.9 MB, less than 100.00% of Python3 online submissions for Day of the Year.
import datetime


class Solution:
    def dayOfYear(self, date: str) -> int:
        year, month, day = map(int, date.split("-"))
        return int((datetime.datetime(year, month, day) - datetime.datetime(year, 1, 1)).days + 1)
