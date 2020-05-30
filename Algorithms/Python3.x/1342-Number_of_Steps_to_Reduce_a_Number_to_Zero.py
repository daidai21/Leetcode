# Runtime: 32 ms, faster than 45.27% of Python3 online submissions for Number of Steps to Reduce a Number to Zero.
# Memory Usage: 13.8 MB, less than 100.00% of Python3 online submissions for Number of Steps to Reduce a Number to Zero.
class Solution:
    def numberOfSteps (self, num: int) -> int:
        res = 0
        while num != 0:
            if num % 2 == 0:
                num = int(num / 2)
            else:
                num -= 1
            res += 1
        return res


if __name__ == "__main__":
    print(Solution().numberOfSteps(14) == 6)
    print(Solution().numberOfSteps(8) == 4)
    print(Solution().numberOfSteps(123) == 12)
