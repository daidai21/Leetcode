# backtracking + dfs
class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        self.res = 0
        self.grid = grid
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] != 0:
                    self.dfs(i, j, 0)
        return self.res

    def dfs(self, i, j, cur_gold):
        self.res = max(self.res, cur_gold)
        if (0 <= i < len(self.grid) and 0 <= j < len(self.grid[0])) and self.grid[i][j] != 0:
            gold = self.grid[i][j]
            for m, n in [(-1, 0), (0, -1), (0, 1), (1, 0)]:
                self.grid[i][j] = 0
                self.dfs(i + m, j + n, cur_gold + gold)
                self.grid[i][j] = gold
