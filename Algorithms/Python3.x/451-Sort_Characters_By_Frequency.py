# Runtime: 36 ms, faster than 98.89% of Python3 online submissions for Sort Characters By Frequency.
# Memory Usage: 13.7 MB, less than 78.57% of Python3 online submissions for Sort Characters By Frequency.
from collections import Counter


class Solution:
    def frequencySort(self, s: str) -> str:
        return ''.join([char * times for char, times in Counter(s).most_common()])
