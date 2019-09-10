# dp
# Runtime: 868 ms, faster than 45.52% of Python3 online submissions for Cherry Pickup.
# Memory Usage: 21.1 MB, less than 33.33% of Python3 online submissions for Cherry Pickup.
class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        if grid[-1][-1] == -1:
            return 0
        self.grid = grid
        self.mem = {}
        self.N = len(grid)
        return max(self.dp(0, 0, 0, 0), 0)

    def dp(self, i1, j1, i2, j2):
        if (i1, j1, i2, j2) in self.mem:
            return self.mem[(i1, j1, i2, j2)]
        if i1 == self.N or j1 == self.N or i2 == self.N or j2 == self.N:
            return -1
        if i1 == self.N - 1 and j1 == self.N - 1 and i2 == self.N - 1 and j2 == self.N - 1:
            return self.grid[-1][-1]
        if self.grid[i1][j1] == -1 or self.grid[i2][j2] == -1:
            return -1
        max_combinate = max([
            self.dp(i1, j1 + 1, i2, j2 + 1),
            self.dp(i1, j1 + 1, i2 + 1, j2),
            self.dp(i1 + 1, j1, i2 + 1, j2),
            self.dp(i1 + 1, j1, i2, j2 + 1),
        ])
        if max_combinate == -1:
            out = -1
        else:
            if i1 == i2 and j1 == j2:
                out = max_combinate + self.grid[i1][j1]
            else:
                out = max_combinate + self.grid[i1][j1] + self.grid[i2][j2]
        self.mem[(i1, j1, i2, j2)] = out
        return out
