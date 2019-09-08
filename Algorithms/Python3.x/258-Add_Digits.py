class Solution:
    def addDigits(self, num: int) -> int:
        while num >= 10:
            tmp = 0
            for n in str(num):
                tmp += int(n)
            num = tmp
        return num


class Solution:
    def addDigits(self, num: int) -> int:
        while num >= 10:
            tmp = 0
            while num > 0:
                tmp += num % 10
                num = int(num / 10)
            num = tmp
        return num


class Solution:
    def addDigits(self, num: int) -> int:
        if num == 0:
            return 0
        else:
            return (num - 1) % 9 + 1


class Solution:
    def addDigits(self, num: int) -> int:
        return (num - 1) % 9 + 1 if num != 0 else 0


class Solution:
    def addDigits(self, num: int) -> int:
        while num >= 10:
            num = sum(int(c) for c in str(num))
        return num
