# Time Limit Exceeded
class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        if n < 2:
            return n
        result = [1]
        for _ in range(n - 1):
            ugly_num = result[-1] + 1
            while not self.is_ugly_num(primes, ugly_num):
                ugly_num += 1
            result.append(ugly_num)
        return result[-1]

    def is_ugly_num(self, primes, num):
        for prime in primes:
            while num % prime == 0:
                num /= prime
            if num == 1:
                return True
        return False


# Runtime: 1156 ms, faster than 15.53% of Python3 online submissions for Super Ugly Number.
# Memory Usage: 17.7 MB, less than 100.00% of Python3 online submissions for Super Ugly Number.
class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        if n < 2:
            return n
        counts = [0] * len(primes)
        result = [None] * n
        result[0] = 1
        for i in range(1, n):
            temp = float("inf")  # min value when update complete this time loop
            for j in range(len(primes)):
                temp = min(temp, primes[j] * result[counts[j]])
            result[i] = temp
            for j in range(len(primes)):  # all equal result will be update, prevent repeat
                if result[counts[j]] * primes[j] == temp:
                    counts[j] += 1
        return result[-1]
