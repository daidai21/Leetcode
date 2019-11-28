# Runtime: 208 ms, faster than 70.80% of Python3 online submissions for Prime Number of Set Bits in Binary Representation.
# Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for Prime Number of Set Bits in Binary Representation.
class Solution:
    def countPrimeSetBits(self, L: int, R: int) -> int:
        primes = (2, 3, 5, 7, 11, 13, 17, 19)
        return sum(bin(x).count('1') in primes for x in range(L, R + 1))


# Runtime: 212 ms, faster than 68.76% of Python3 online submissions for Prime Number of Set Bits in Binary Representation.
# Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for Prime Number of Set Bits in Binary Representation.
class Solution:
    def countPrimeSetBits(self, L: int, R: int) -> int:
        return sum(bin(x).count('1') in (2, 3, 5, 7, 11, 13, 17, 19) for x in range(L, R + 1))
