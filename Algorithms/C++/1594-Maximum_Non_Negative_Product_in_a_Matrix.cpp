// 1594. Maximum Non Negative Product in a Matrix

// Runtime: 12 ms, faster than 15.10% of C++ online submissions for Maximum Non Negative Product in a Matrix.
// Memory Usage: 10.2 MB, less than 49.00% of C++ online submissions for Maximum Non Negative Product in a Matrix.
class Solution {
public:
    int maxProductPath(vector<vector<int>>& grid) {
        vector<vector<long long int>> max_path(grid.size(), vector<long long int>(grid[0].size(), 0));
        vector<vector<long long int>> min_path(grid.size(), vector<long long int>(grid[0].size(), 0));
        for (int i = 0; i < grid.size(); ++i) {
            for (int j = 0; j < grid[0].size(); ++j) {
                if (i == 0 && j == 0) {
                    max_path[i][j] = grid[i][j];
                    min_path[i][j] = grid[i][j];
                } else if (i == 0) {
                    max_path[i][j] = max(grid[i][j] * max_path[i][j - 1], 
                                         grid[i][j] * min_path[i][j - 1]);
                    min_path[i][j] = min(grid[i][j] * max_path[i][j - 1], 
                                         grid[i][j] * min_path[i][j - 1]);
                } else if (j == 0) {
                    max_path[i][j] = max(grid[i][j] * max_path[i - 1][j], 
                                         grid[i][j] * min_path[i - 1][j]);
                    min_path[i][j] = min(grid[i][j] * max_path[i - 1][j], 
                                         grid[i][j] * min_path[i - 1][j]);                    
                } else {
                    max_path[i][j] = max(max(grid[i][j] * max_path[i][j - 1], grid[i][j] * max_path[i - 1][j]),
                                         max(grid[i][j] * min_path[i][j - 1], grid[i][j] * min_path[i - 1][j]));
                    min_path[i][j] = min(min(grid[i][j] * max_path[i][j - 1], grid[i][j] * max_path[i - 1][j]),
                                         min(grid[i][j] * min_path[i][j - 1], grid[i][j] * min_path[i - 1][j]));
                }
            }
        }
        return max(-1, 
                   (int) (max(max_path[grid.size() - 1][grid[0].size() - 1], 
                             min_path[grid.size() - 1][grid[0].size() - 1]) % 1000000007));
    }
};
