class Solution:
    def convertToTitle(self, n: int) -> str:
        return "" if n == 0 else self.convertToTitle(int((n - 1) / 26)) + chr((n - 1) % 26 + ord('A'))


class Solution:
    def convertToTitle(self, n: int) -> str:
        res = ""
        while n:
            tmp = n % 26
            n = int(n / 26)
            if tmp == 0:
                res += 'Z'
                n -= 1;
            else:
                res += chr(tmp + ord('A') - 1)
        return res[::-1]
