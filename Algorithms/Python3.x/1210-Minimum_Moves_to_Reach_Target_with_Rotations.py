# bfs
# Runtime: 288 ms, faster than 100.00% of Python3 online submissions for Minimum Moves to Reach Target with Rotations.
# Memory Usage: 15.9 MB, less than 100.00% of Python3 online submissions for Minimum Moves to Reach Target with Rotations.
class Solution:
    def minimumMoves(self, grid: List[List[int]]) -> int:
        cur = [(0, 0, 0)]
        cnt = 0
        n = len(grid)
        seen = set([(0, 0, 0)])  # tail row, tail col, horizontal or verticle
        while cur and (n - 1, n - 2, 0) not in cur:
            cnt += 1
            tmp = []
            for x, y, dx in cur:
                if dx == 0:  # verticle
                    if y + 2 < n and grid[x][y + 2] == 0:
                        tmp += [(x, y + 1, dx)]
                    if x + 1 < n and (grid[x + 1][y] + grid[x + 1][y + 1]) == 0:
                        tmp += [(x, y, 1), (x + 1, y, 0)]
                else:  # horizontal
                    if x + 2 < n and grid[x + 2][y] == 0:
                        tmp += [(x + 1, y, dx)]
                    if y + 1 < n and (grid[x][y + 1] + grid[x + 1][y + 1]) == 0:
                        tmp += [(x, y, 0), (x, y + 1, 1)]
            cur = set(tmp) - seen
            seen |= cur  # union
        return cnt if cur else - 1
