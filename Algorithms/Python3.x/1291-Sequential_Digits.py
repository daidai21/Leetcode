# Runtime: 28 ms, faster than 58.99% of Python3 online submissions for Sequential Digits.
# Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Sequential Digits.
class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        res = []
        for start in range(10):
            num = start
            for length in range(len(str(high))):
                if int(str(num)[-1]) + 1 > 9:
                    pass
                else:
                    num = num * 10 + int(str(num)[-1]) + 1
                if len(str(num)) >= len(str(low)):
                    if low <= num <= high:
                        res.append(num)
        return sorted(list(set(res)))
