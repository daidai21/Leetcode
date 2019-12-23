# Time Limit Exceeded
class Solution:
    def bulbSwitch(self, n: int) -> int:
        bulbs = [False] * n
        for step in range(1, n + 1):
            for idx in range(n):
                if (idx + 1) % step == 0:
                    bulbs[idx] = not bulbs[idx]
        return sum(bulbs)


# Runtime: 48 ms, faster than 5.83% of Python3 online submissions for Bulb Switcher.
# Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for Bulb Switcher.
class Solution:
    def bulbSwitch(self, n: int) -> int:
        return int(n ** 0.5)


# Runtime: 28 ms, faster than 81.13% of Python3 online submissions for Bulb Switcher.
# Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for Bulb Switcher.
import math


class Solution:
    def bulbSwitch(self, n: int) -> int:
        return int(math.sqrt(n))
