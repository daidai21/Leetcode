# Runtime: 96 ms, faster than 53.76% of Python3 online submissions for Surface Area of 3D Shapes.
# Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Surface Area of 3D Shapes.
class Solution:
    def surfaceArea(self, grid: List[List[int]]) -> int:
        area = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                # add top and bottom area
                area += 2 * (grid[row][col] != 0)
                # add left side area
                area += abs(grid[row][col] - grid[row][col - 1]) if col != 0 else grid[row][col]
                # add up side area
                area += abs(grid[row][col] - grid[row - 1][col]) if row != 0 else grid[row][col]
        # add all 3D right side
        for row in range(len(grid)):
            area += grid[row][-1]
        # add all 3D down sige
        for col in range(len(grid[0])):
            area += grid[-1][col]
        return area
