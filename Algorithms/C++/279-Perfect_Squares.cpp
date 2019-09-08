// Runtime: 104 ms, faster than 54.49% of C++ online submissions for Perfect Squares.
// Memory Usage: 11.3 MB, less than 69.23% of C++ online submissions for Perfect Squares.
class Solution {
public:
    int numSquares(int n) {
        vector<int> dp(n + 1, INT_MAX);
        dp[0] = 0;
        for (int i = 1; i < n + 1; ++i) {
            int j = 1;
            while (j * j <= i) {
                dp[i] = min(dp[i], dp[i - j * j] + 1);
                ++j;
            }
        }
        return dp[n];
    }
};
