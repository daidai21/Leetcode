# dfs
class Solution:
    def numIslands(self, grid: 'List[List[str]]') -> 'int':
        if grid == []: return 0
        def dfs(i, j, n, m):
            if i < 0 or j < 0 or i >= n or j >= m or grid[i][j] == "0" or grid[i][j] == "-1": return 
            grid[i][j] = "-1"
            dfs(i + 1, j, n, m)
            dfs(i - 1, j, n, m)
            dfs(i, j + 1, n, m)
            dfs(i, j - 1, n, m)

        num_islands = 0
        n, m = len(grid), len(grid[0])
        for i in range(n):
            for j in range(m):
                if grid[i][j] == "1":
                    dfs(i, j, n, m)
                    num_islands += 1
        return num_islands
