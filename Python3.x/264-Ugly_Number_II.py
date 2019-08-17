# Runtime: 152 ms, faster than 80.61% of Python3 online submissions for Ugly Number II.
# Memory Usage: 13.9 MB, less than 20.00% of Python3 online submissions for Ugly Number II.
class Solution:
    def nthUglyNumber(self, n: int) -> int:
        if n <= 0:
            return None
        if n == 1:
            return 1;
        t2, t3, t5 = 0, 0, 0
        dp = [0] * n
        dp[0] = 1
        for i in range(1, n):
            dp[i] = min(dp[t2] * 2, dp[t3] * 3, dp[t5] * 5)
            if dp[i] == dp[t2] * 2:
                t2 += 1
            if dp[i] == dp[t3] * 3:
                t3 += 1
            if dp[i] == dp[t5] * 5:
                t5 += 1
        return dp[-1]


# Time Limit Exceeded
class Solution:
    def nthUglyNumber(self, n: int) -> int:
        num, step = 1, 0
        while step != n:
            if self.isUgly(num):
                step += 1
            num += 1
        return num - 1

    def isUgly(self, num: int) -> bool:
        if num == 0:
            return False
        while num % 2 == 0:
            num /= 2
        while num % 3 == 0:
            num /= 3
        while num % 5 == 0:
            num /= 5
        return num == 1
