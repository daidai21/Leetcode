# Time Limit Exceeded
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str, 
                                       idx1: int = 0, idx2: int = 0) -> int:
        if idx1 >= len(text1) or idx2 >= len(text2):
            return 0
        elif text1[idx1] == text2[idx2]:
            return 1 + self.longestCommonSubsequence(text1, text2, idx1 + 1, idx2 + 1)
        else:
            return max(self.longestCommonSubsequence(text1, text2, idx1 + 1, idx2),
                       self.longestCommonSubsequence(text1, text2, idx1, idx2 + 1))


# Runtime: 428 ms, faster than 85.21% of Python3 online submissions for Longest Common Subsequence.
# Memory Usage: 21.5 MB, less than 69.03% of Python3 online submissions for Longest Common Subsequence.
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = [[0] * (len(text2) + 1) for _ in range(len(text1) + 1)]
        for i in range(1, len(text1) + 1):
            for j in range(1, len(text2) + 1):
                if text1[i - 1] == text2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        return dp[-1][-1]
