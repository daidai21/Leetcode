class Solution:
    def isPalindrome(self, x: int) -> bool:
        return str(x) == str(x)[::-1]


class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        p, res = x, 0
        while p:
            res = res * 10 + p % 10
            p = int(p / 10)
        return res == x
