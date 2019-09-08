# Time Limit Exceeded
class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        res = [0] * n
        for i, j, k in bookings:
            for idx in range(i - 1, j):
                res[idx] += k
        return res


class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        res = [0] * n
        for i, j, k in bookings:
            res[i - 1] += k
            if j < n:
                res[j] -= k
        for i in range(1, n):
            res[i] += res[i - 1]
        return res

