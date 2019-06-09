# Runtime: 48 ms, faster than 38.12% of Python3 online submissions for Happy Number.
# Memory Usage: 13.4 MB, less than 5.04% of Python3 online submissions for Happy Number.
class Solution:
    def isHappy(self, n: int) -> bool:
        mem = set()
        while n != 1:
            n = sum([int(i) ** 2 for i in str(n)])
            if n in mem: return False
            else: mem.add(n)
        else: return True
