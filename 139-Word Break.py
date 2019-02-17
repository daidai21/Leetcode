# dp
# Runtime: 44 ms, faster than 70.03% of Python3 online submissions for Word Break.
# Memory Usage: 12.5 MB, less than 100.00% of Python3 online submissions for Word Break.
class Solution:
    def wordBreak(self, s: 'str', wordDict: 'List[str]') -> 'bool':
        dp = [False] * (len(s)+1)
        dp[0] = True
        for i in range(1, len(s)+1):
            for j in range(i):
                if dp[j] and s[j:i] in wordDict:
                    dp[i] = True
                    break
        return dp[-1]
