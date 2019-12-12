# Binary Search
import math


class Solution:
    def minEatingSpeed(self, piles: List[int], H: int) -> int:
        left, right = 1, max(piles)
        while left < right:
            mid = (left + right) // 2
            need_H = 0
            for pile in piles:
                need_H += math.ceil(pile / mid)
            if need_H > H:
                left = mid + 1
            else:
                right = mid
        return left


# Runtime: 552 ms, faster than 62.09% of Python3 online submissions for Koko Eating Bananas.
# Memory Usage: 14 MB, less than 100.00% of Python3 online submissions for Koko Eating Bananas.
# Binary Search
class Solution:
    def minEatingSpeed(self, piles: List[int], H: int) -> int:
        left, right = 1, max(piles)
        while left < right:
            mid = (left + right) // 2
            need_H = 0
            for pile in piles:
                need_H += int(pile / mid + 0.99)  # FIXME: ceil() Not rigorous
            if need_H > H:
                left = mid + 1
            else:
                right = mid
        return left
