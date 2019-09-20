# Runtime: 88 ms, faster than 56.80% of Python3 online submissions for Projection Area of 3D Shapes.
# Memory Usage: 13.8 MB, less than 12.50% of Python3 online submissions for Projection Area of 3D Shapes.
class Solution:
    def projectionArea(self, grid: List[List[int]]) -> int:
        area = 0
        for i in grid:  # over look
            for j in i:
                area += j != 0
        area += sum([max(s) for s in grid])  # left look
        for col in range(len(grid)):  # main look
            high = 0
            for row in range(len(grid)):
                high = max(high, grid[row][col])
            area += high
        return area
