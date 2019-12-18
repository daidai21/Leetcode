# Runtime: 580 ms, faster than 10.76% of Python3 online submissions for Shift 2D Grid.
# Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Shift 2D Grid.
class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        for _ in range(k):
            temp = grid[len(grid) - 1][len(grid[0]) - 1]
            for row in range(len(grid) - 1, -1, -1):
                for col in range(len(grid[0]) - 1, -1, -1):
                    if col == 0:
                        if row == 0:
                            pass
                        else:
                            grid[row][col] = grid[row - 1][-1]
                    else:
                        grid[row][col] = grid[row][col - 1]
            grid[0][0] = temp
        return grid


# Runtime: 164 ms, faster than 85.83% of Python3 online submissions for Shift 2D Grid.
# Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Shift 2D Grid.
class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        vec = [val for line in grid for val in line]
        k = k % (len(grid) * len(grid[0]))
        vec = vec[-k:] + vec[:-k]
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                grid[row][col] = vec[row * len(grid[0]) + col]
        return grid


# Runtime: 200 ms, faster than 31.30% of Python3 online submissions for Shift 2D Grid.
# Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Shift 2D Grid.
class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        self.grid = grid
        self.rows, self.cols = len(grid), len(grid[0])
        k %= self.rows * self.cols
        self.reverse(0, self.rows * self.cols - 1)
        self.reverse(0, k - 1)
        self.reverse(k, self.rows * self.cols - 1)
        return self.grid

    def reverse(self, lo: int, hi: int) -> None:
        while lo < hi:
            r, c, i, j = lo // self.cols, lo % self.cols, hi // self.cols, hi % self.cols
            self.grid[r][c], self.grid[i][j] = self.grid[i][j], self.grid[r][c]
            lo += 1
            hi -= 1
