// Runtime: 12 ms, faster than 50.16% of C++ online submissions for Minimum Path Sum.
// Memory Usage: 10.7 MB, less than 65.17% of C++ online submissions for Minimum Path Sum.
class Solution {
public:
    int minPathSum(vector<vector<int>>& grid) {
        vector<vector<int>> dp(grid.size(), vector<int>(grid[0].size()));
        dp[0][0] = grid[0][0];
        for (int i = 1; i < grid.size(); ++i)
            dp[i][0] = grid[i][0] + dp[i - 1][0];
        for (int i = 1; i < grid[0].size(); ++i)
            dp[0][i] = grid[0][i] + dp[0][i - 1];
        for (int i = 1; i < grid.size(); ++i)
            for (int j = 1; j < grid[0].size(); ++j)
                dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + grid[i][j];
        return dp[grid.size() - 1][grid[0].size() - 1];
    }
};


// Runtime: 4 ms, faster than 99.34% of C++ online submissions for Minimum Path Sum.
// Memory Usage: 10.4 MB, less than 100.00% of C++ online submissions for Minimum Path Sum.
class Solution {
public:
    int minPathSum(vector<vector<int>>& grid) {
        vector<int> dp(grid[0].size());
        dp[0] = grid[0][0];
        for (int i = 1; i < grid[0].size(); ++i)
            dp[i] = grid[0][i] + dp[i - 1];
        for (int i = 1; i < grid.size(); ++i) { // row
            dp[0] += grid[i][0];
            for (int j = 1; j < grid[0].size(); ++j) // col
                dp[j] = min(dp[j - 1], dp[j]) + grid[i][j];
        }
        return dp[grid[0].size() - 1];
    }
};
