# https://leetcode.cn/problems/combinations/

"""
给定两个整数 n 和 k，返回范围 [1, n] 中所有可能的 k 个数的组合。

你可以按 任何顺序 返回答案。
"""

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        self.res = []
        self.n = n
        self.k = k
        self.dfs([], 1, k)
        return self.res

    
    def dfs(self, cur, curNum, curK):
        if len(cur) == self.k:
            self.res.append(cur)
            return
        if curK == 0:
            return
        if curNum > self.n:
            return
        self.dfs(cur, curNum + 1, curK)
        self.dfs(cur + [curNum], curNum + 1, curK - 1)
