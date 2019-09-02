# Time Limit Exceeded
# probably have bug
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        self.result = 0
        self.arrange_combine(s, t, "")
        return self.result

    def arrange_combine(self, s, t, curr):
        if curr == t:
            self.result += 1
        if s == "":
            return 
        else:
            for i, c in enumerate(s):
                self.arrange_combine(s[i + 1:], t, curr + c)


# Runtime: 144 ms, faster than 64.79% of Python3 online submissions for Distinct Subsequences.
# Memory Usage: 17.9 MB, less than 57.14% of Python3 online submissions for Distinct Subsequences.
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        dp = [[0] * (len(s) + 1) for _ in range(len(t) + 1)]
        for j in range(len(s) + 1):
            dp[0][j] = 1
        for i in range(1, len(t) + 1):
            for j in range(1, len(s) + 1):
                if t[i - 1] == s[j - 1]:
                    dp[i][j] = dp[i][j - 1] + dp[i - 1][j - 1]
                else:
                    dp[i][j] = dp[i][j - 1]
        return dp[-1][-1]


# Runtime: 112 ms, faster than 82.50% of Python3 online submissions for Distinct Subsequences.
# Memory Usage: 14.1 MB, less than 57.14% of Python3 online submissions for Distinct 
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        dp = [1] * (len(s) + 1)
        for i in range(1, len(t) + 1):
            temp = [0] * (len(s) + 1)
            for j in range(1, len(s) + 1):
                if t[i - 1] == s[j - 1]:
                    temp[j] = temp[j - 1] + dp[j - 1]
                else:
                    temp[j] = temp[j - 1]
            dp = temp
        return dp[-1]
