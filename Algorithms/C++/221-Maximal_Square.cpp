// Runtime: 20 ms, faster than 76.78% of C++ online submissions for Maximal Square.
// Memory Usage: 11.2 MB, less than 48.15% of C++ online submissions for Maximal Square.
class Solution {
public:
    int maximalSquare(vector<vector<char>>& matrix) {
        if (matrix.empty())
            return 0;
        int res = 0;
        vector<vector<int>> dp(matrix.size(), vector<int> (matrix[0].size(), 0));
        for (int row = 0; row < matrix.size(); ++row)
            for (int col = 0; col < matrix[0].size(); ++col) {
                if (!row || !col || matrix[row][col] == '0')
                    dp[row][col] = matrix[row][col] - '0';
                else
                    dp[row][col] = min(dp[row - 1][col], min(dp[row][col - 1], dp[row - 1][col - 1])) + 1;
                res = max(res, dp[row][col]);
            }
        return res * res;
    }
};
