# Runtime: 172 ms, faster than 13.49% of Python3 online submissions for Max Area of Island.
# Memory Usage: 16.3 MB, less than 60.98% of Python3 online submissions for Max Area of Island.

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        self.grid = grid
        self.seen = set()
        self.rowLen = len(grid)
        self.colLen = len(grid[0])
        res = 0
        for row in range(self.rowLen):
            for col in range(self.colLen):
                res = max(res, self.area(row, col))
        return res

    def area(self, row, col):
        if 0 <= row < self.rowLen and 0 <= col < self.colLen \
                and (row, col) not in self.seen and self.grid[row][col] == 1:
            self.seen.add((row, col))
            return 1 + self.area(row + 1, col) + self.area(row - 1, col) \
                + self.area(row, col + 1) + self.area(row, col - 1)
        return 0
