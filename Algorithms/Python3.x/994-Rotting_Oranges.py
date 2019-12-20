# Runtime: 40 ms, faster than 99.12% of Python3 online submissions for Rotting Oranges.
# Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for Rotting Oranges.
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        Q = collections.deque([])
        cnt = 0  # fresh orange
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    cnt += 1
                if grid[i][j] == 2:
                    Q.append((i, j))
        res = 0
        while Q:
            for _ in range(len(Q)):
                i, j = Q.popleft()
                for x, y in ((i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)):
                    if 0 <= x < n and 0 <= y < m and grid[x][y] == 1:
                        grid[x][y] = 2
                        cnt -= 1
                        Q.append((x, y))
            res += 1
        return max(0, res - 1) if cnt == 0 else -1
