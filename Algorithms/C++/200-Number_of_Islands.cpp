// Runtime: 16 ms, faster than 59.75% of C++ online submissions for Number of Islands.
// Memory Usage: 10.5 MB, less than 100.00% of C++ online submissions for Number of Islands.
class Solution {
public:
    void dfs(vector<vector<char>>& grid, int len_row, int len_col, int i, int j) {
        if (0 <= i && i < len_row && 0 <= j && j < len_col && grid[i][j] == '1') {
            grid[i][j] = '2';
            dfs(grid, len_row, len_col, i + 1, j);
            dfs(grid, len_row, len_col, i - 1, j);
            dfs(grid, len_row, len_col, i, j + 1);
            dfs(grid, len_row, len_col, i, j - 1);
        }
    }
    int numIslands(vector<vector<char>>& grid) {
        if (grid.empty())
            return 0;
        int len_row = grid.size(),
            len_col = grid[0].size();
        int islands = 0;
        for (int i = 0; i < len_row; ++i)
            for (int j = 0; j < len_col; ++j)
                if (grid[i][j] == '1') {
                    dfs(grid, len_row, len_col, i, j);
                    ++islands;
                }
        return islands;
    }
};
