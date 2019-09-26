# Time Limit Exceeded
class Solution:
    def minCut(self, s: str) -> int:
        if self.judge(s):
            return 0
        self.cut_s = []
        self.dfs(s, [])
        return min([len(l) for l in self.cut_s]) - 1

    def dfs(self, s, cur):
        if not s:
            self.cut_s.append(cur)
            return
        else:
            for i in range(1, len(s) + 1):
                if self.judge(s[:i]):
                    self.dfs(s[i:], cur + [s[:i]])

    def judge(self, s):
        return s == s[::-1]


# dp
# Runtime: 892 ms, faster than 20.26% of Python3 online submissions for Palindrome Partitioning II.
# Memory Usage: 13.7 MB, less than 90.00% of Python3 online submissions for Palindrome Partitioning II.
class Solution:
    def minCut(self, s: str) -> int:
        cut = [i for i in range(-1, len(s))]
        for i in range(len(s)):
            for j in range(i, len(s)):
                if s[i:j] == s[j:i:-1]:
                    cut[j + 1] = min(cut[j + 1], cut[i] + 1)
        return cut[-1]
