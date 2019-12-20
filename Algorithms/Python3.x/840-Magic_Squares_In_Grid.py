# Runtime: 40 ms, faster than 55.99% of Python3 online submissions for Magic Squares In Grid.
# Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Magic Squares In Grid.
class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        cnt_valid = 0
        temp_grid = [[0] * 3 for _ in range(3)]
        for row in range(len(grid) - 3 + 1):
            for col in range(len(grid[0]) - 3 + 1):
                for i in range(3):
                    for j in range(3):
                        temp_grid[i][j] = grid[row + i][col + j]
                cnt_valid += self.magic_squares_valid(temp_grid)
        return cnt_valid

    def magic_squares_valid(self, grid):
        # check number repeat
        nums = set()
        for line in grid:
            for num in line:
                nums.add(num)
        if nums != set([1, 2, 3, 4, 5, 6, 7, 8, 9]):
            return False
        # check row sum
        for i in range(3):
            if sum(grid[i]) != 15:
                return False
        # check column sum
        for j in range(3):
            if sum([grid[0][j], grid[1][j], grid[2][j]]) != 15:
                return False
        # check diagonal sum
        if sum([grid[0][0], grid[1][1], grid[2][2]]) != 15:
            return False
        if sum([grid[0][2], grid[1][1], grid[2][0]]) != 15:
            return False
        return True
