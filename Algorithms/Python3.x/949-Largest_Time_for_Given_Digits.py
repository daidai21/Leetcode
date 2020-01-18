from typing import List


# Runtime: 32 ms, faster than 53.91% of Python3 online submissions for Largest Time for Given Digits.
# Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Largest Time for Given Digits.
from itertools import permutations


class Solution:
    def largestTimeFromDigits(self, A: List[int]) -> str:
        res = -1
        for h1, h2, m1, m2 in permutations(A):
            hours = h1 * 10 + h2
            mins = m1 * 10 + m2
            times = 60 * hours + mins
            if 0 <= hours < 24 and 0 <= mins < 60 and times > res:
                res = times
        return "{:02}:{:02}".format(res // 60, res % 60) if res >= 0 else ""


print(Solution().largestTimeFromDigits([1,2,3,4]))
print(Solution().largestTimeFromDigits([5,5,5,5]))
