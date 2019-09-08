# Time Limit Exceeded
class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        result = 0
        for i in range(10 ** n):
            result += len(set(str(i))) == len(str(i))
        return result


# Runtime: 36 ms, faster than 65.03% of Python3 online submissions for Count Numbers with Unique Digits.
# Memory Usage: 13.8 MB, less than 50.00% of Python3 online submissions for Count Numbers with Unique Digits.
class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        if n == 0:
            return 1
        res = 10
        temp = 9
        for i in range(2, n + 1):
            temp *= 11 - i
            res += temp
        return res
