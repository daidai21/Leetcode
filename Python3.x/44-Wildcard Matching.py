# Runtime: 220 ms, faster than 69.81% of Python3 online submissions for Wildcard Matching.
# Memory Usage: 13.3 MB, less than 79.83% of Python3 online submissions for Wildcard Matching.
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        len_s = len(s)
        if len(p) - p.count('*') > len_s:
            return False
        dp = [True] + [False] * len_s
        for i in p:
            if i != '*':
                for n in reversed(range(len_s)):
                    dp[n + 1] = dp[n] and (i == s[n] or i == '?')
            else:
                for n in range(1, len_s + 1):
                    dp[n] = dp[n - 1] or dp[n]
            dp[0] = dp[0] and i == '*'
        return dp[-1]
