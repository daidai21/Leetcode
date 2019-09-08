# Time Limit Exceeded
class Solution:
    def superPow(self, a: int, b: List[int]) -> int:
        if len(b) == 0:
            return None
        if len(b) == 1:
            return a ** b[0] % 1337
        temp = b[0]
        idx = 1
        while idx < len(b):
            temp = temp * 10 + b[idx]
            idx += 1
        return a ** temp % 1337


# Time Limit Exceeded
class Solution:
    def superPow(self, a: int, b: List[int]) -> int:
        if len(b) == 0:
            return None
        a = a % 1337
        if len(b) == 1:
            return a ** b[0] % 1337
        temp = b[0]
        idx = 1
        while idx < len(b):
            temp = temp * 10 + b[idx]
            idx += 1
        return a ** temp % 1337


"""
a ^ b mod c == (a mod c) ^ b mod c
"""


# Runtime: 184 ms, faster than 42.53% of Python3 online submissions for Super Pow.
# Memory Usage: 14.9 MB, less than 25.00% of Python3 online submissions for Super Pow.
class Solution:
    def superPow(self, a: int, b: List[int]) -> int:
        if not b:
            return 1
        else:
            return pow(a, b.pop(), 1337) * self.superPow(pow(a, 10, 1337), b) % 1337


"""
n1*n2 % 1337 == (n1 % 1337)*(n2 % 1337) % 1337
If b = m*10 + d, we have a**b == (a**d)*(a**10)**m
"""
