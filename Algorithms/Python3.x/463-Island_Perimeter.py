# Runtime: 600 ms, faster than 47.41% of Python3 online submissions for Island Perimeter.
# Memory Usage: 13.8 MB, less than 25.00% of Python3 online submissions for Island Perimeter.
class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        perimeters = 0
        len_row, len_col = len(grid), len(grid[0])
        for row in range(len_row):
            for col in range(len_col):
                if grid[row][col] == 0:  # water
                    if row > 0:  # up
                        perimeters += grid[row - 1][col]
                    if row < len_row - 1:  # down
                        perimeters += grid[row + 1][col]
                    if col > 0:  # left
                        perimeters += grid[row][col - 1]
                    if col < len_col - 1:  # right
                        perimeters += grid[row][col + 1]
                else:  # land
                    perimeters += row == 0
                    perimeters += row == len_row - 1
                    perimeters += col == 0
                    perimeters += col == len_col - 1
        return perimeters


# Runtime: 536 ms, faster than 91.59% of Python3 online submissions for Island Perimeter.
# Memory Usage: 14.3 MB, less than 16.67% of Python3 online submissions for Island Perimeter.
class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        area, connect = 0, 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1:
                    area += 1
                    if row > 0 and grid[row - 1][col]:
                        connect += 1
                    if col > 0 and grid[row][col - 1]:
                        connect += 1
        return 4 * area - 2 * connect
