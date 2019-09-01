# dp
# Runtime: 52 ms, faster than 36.76% of Python3 online submissions for Interleaving String.
# Memory Usage: 13.9 MB, less than 16.67% of Python3 online submissions for Interleaving String.
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3) or sorted(s1 + s2) != sorted(s3):
            return False
        if s1 == '' and s2 == s3 or s2 == '' and s1 == s3:
            return True
        dp = [[False] * (len(s2) + 1)] * (len(s1) + 1)
        for i1 in range(len(s1) + 1):
            for i2 in range(len(s2) + 1):
                if i1 == 0 and i2 == 0:
                    dp[i1][i2] = True
                elif i1 == 0:
                    dp[i1][i2] = dp[i1][i2 - 1] and s2[i2 - 1] == s3[i1 + i2 - 1]
                elif i2 == 0:
                    dp[i1][i2] = dp[i1 - 1][i2] and s1[i1 - 1] == s3[i1 + i2 - 1]
                else:
                    dp[i1][i2] = (dp[i1 - 1][i2] and s1[i1 - 1] == s3[i1 + i2 - 1]) or \
                             (dp[i1][i2 - 1] and s2[i2 - 1] == s3[i1 + i2 - 1])
        return dp[-1][-1]
