# Time Limit Exceeded
# Brute Force
class Solution:
    def reachNumber(self, target: int) -> int:
        cur = [0]
        n = 1
        while True:
            new_cur = []
            for idx in cur:
                if idx + n == target or idx - n == target:
                    return n
                new_cur.append(idx + n)
                new_cur.append(idx - n)
            cur = new_cur
            n += 1


# Runtime: 108 ms, faster than 59.80% of Python3 online submissions for Reach a Number.
# Memory Usage: 12.6 MB, less than 100.00% of Python3 online submissions for Reach a Number.
class Solution:
    def reachNumber(self, target: int) -> int:
        target = abs(target)
        k = 0
        while target > 0:
            k += 1
            target -= k
        return k if target % 2 == 0 else k + 1 + k % 2
