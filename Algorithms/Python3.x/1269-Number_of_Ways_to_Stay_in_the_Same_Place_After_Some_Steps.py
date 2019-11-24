class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        MOD = 10 ** 9 + 7
        if arrLen <= 1:
            return arrLen
        lst = [0] * arrLen
        lst[0], lst[1] = 1, 1
        for j in range(1, steps):
            temp = [0] * arrLen
            for i in range(min(arrLen, steps)):
                ans = lst[i]
                if i > 0:
                    ans = (ans + lst[i - 1]) % MOD
                if i < arrLen - 1:
                    ans = (ans + lst[i + 1]) % MOD
                temp[i] = ans
            lst = temp
        return lst[0]
