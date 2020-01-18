# Runtime: 28 ms, faster than 59.85% of Python3 online submissions for Airplane Seat Assignment Probability.
# Memory Usage: 12.6 MB, less than 100.00% of Python3 online submissions for Airplane Seat Assignment Probability.
class Solution:
    def nthPersonGetsNthSeat(self, n: int) -> float:
        return 1.0 if n == 1 else 0.5
