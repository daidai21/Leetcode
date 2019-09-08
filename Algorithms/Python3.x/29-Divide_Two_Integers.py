# Time Limit Exceeded
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend == 0 or divisor == 0:
            return 0
        elif (dividend > 0 and divisor > 0) or (dividend < 0 and divisor < 0):
            sign = True
        elif (dividend > 0 and divisor < 0) or (dividend < 0 and divisor > 0):
            sign = False
        dividend, divisor = abs(dividend), abs(divisor)
        res, add = 0, 0
        while add <= dividend:
            res, add = res + 1, add + divisor
        return res - 1 if sign else -(res - 1)


# Runtime: 36 ms, faster than 83.42% of Python3 online submissions for Divide Two Integers.
# Memory Usage: 13.4 MB, less than 18.57% of Python3 online submissions for Divide Two Integers.
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend == 0 or divisor == 0:
            return 0
        sign = (dividend > 0) == (divisor > 0)
        dividend, divisor = abs(dividend), abs(divisor)
        res = 0
        while dividend >= divisor:
            tmp, i = divisor, 1
            while dividend >= tmp:
                dividend, res = dividend - tmp, res + i
                i, tmp = i * 2, tmp * 2
        res = res if sign else -res
        return min(max(-2 ** 31, res), 2 ** 31 - 1)
