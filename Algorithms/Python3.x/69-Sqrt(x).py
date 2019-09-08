# Runtime: 36 ms, faster than 95.79% of Python3 online submissions for Sqrt(x).
# Memory Usage: 13.4 MB, less than 7.56% of Python3 online submissions for Sqrt(x).
class Solution:
    def mySqrt(self, x: int) -> int:
        return int(x ** 0.5)


# Runtime: 52 ms, faster than 53.61% of Python3 online submissions for Sqrt(x).
# Memory Usage: 13.2 MB, less than 70.31% of Python3 online submissions for Sqrt(x).
class Solution:
    def mySqrt(self, x: int) -> int:
        l, r = 0, x
        while l <= r:
            mid =  l + (r - l) // 2
            if mid ** 2 <= x < (mid + 1) ** 2:
                return mid
            elif x < mid ** 2:
                r = mid
            else:
                l = mid + 1
