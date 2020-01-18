class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        if num < 0:
            return False
        sum_divisors = 0
        for divisor in range(1, num):
            if num % divisor == 0:
                sum_divisors += divisor
        return sum_divisors == num


class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        if num < 0:
            return False
        sum_divisors = 0
        for divisor in range(1, num):
            if num % divisor == 0:
                sum_divisors += divisor
            if sum_divisors > num:
                return False
        return sum_divisors == num


# Runtime: 36 ms, faster than 64.05% of Python3 online submissions for Perfect Number.
# Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Perfect Number.
class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        if num <= 0:
            return False
        sum_divisors = 0
        for divisor in range(1, int(num ** 0.5) + 1):
            if num % divisor == 0:
                sum_divisors += divisor
                if divisor ** 2 != num:
                    sum_divisors += num / divisor
        return sum_divisors - num == num


# Runtime: 20 ms, faster than 99.83% of Python3 online submissions for Perfect Number.
# Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for Perfect Number.
class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        return num in (6, 28, 496, 8128, 33550336)


print(Solution().checkPerfectNumber(28))
