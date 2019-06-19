# dfs
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        self.res = []
        self.dfs(s, [])
        return self.res

    def dfs(self, s, tmp):
        if not s:
            self.res.append(tmp)
            return
        for i in range(1, len(s) + 1):
            if self.judge(s[:i]):
                self.dfs(s[i:], tmp + [s[:i]])

    def judge(self, s):
        return s == s[::-1]

