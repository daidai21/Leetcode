# dp
class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        length = len(s)
        dp = [1] * length  # 初始化dp数组
        for j in range(1, length):  # 左指针
            left = dp[j]
            for i in reversed(range(0, j)):  # 右指针
                right = dp[i]
                if s[i] == s[j]:  # 字符相等
                    if i + 1 <= j - 1:
                        dp[i] = 2 + left  # 加上之前的
                    else:
                        dp[i] = 2  # 第一次回文
                else:
                    dp[i] = max(dp[i + 1], dp[i])  # 更新
                left = right
        return dp[0]


# space: O(n)
# time: O(n^2)
class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        length = len(s)
        dp = [1] * length  # dp list
        for j in range(1, length):  # point left
            left = dp[j]
            for i in reversed(range(0, j)):  # point right
                right = dp[i]
                if s[i] == s[j]: dp[i] = 2 + left if i + 1 <= j - 1 else 2
                else: dp[i] = max(dp[i + 1], dp[i])
                left = right
        return dp[0]
