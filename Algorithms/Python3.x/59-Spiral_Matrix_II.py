class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        res = [[None] * n for _ in range(n)]
        col, row = 0, 0
        direction = 1  # 1 is right
        for i in range(1, n * n + 1):
            print(i, res)
            res[row][col] = i
            if direction % 4 == 1:  # right
                if col + 1 < n and res[row][col + 1] is None:
                    col += 1
                else:
                    direction += 1
                    row += 1
            elif direction % 4 == 2:  # down
                if row + 1 < n and res[row + 1][col] is None:
                    row += 1
                else:
                    direction += 1
                    col -= 1
            elif direction % 4 == 3:  # left
                if col - 1 >= 0 and res[row][col - 1] is None:
                    col -= 1
                else:
                    direction += 1
                    row -= 1
            else:  # up
                if row - 1 >= 0 and res[row - 1][col] is None:
                    row -= 1
                else:
                    direction += 1
                    col += 1
        return res
