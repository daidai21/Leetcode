// Runtime: 192 ms, faster than 71.46% of C++ online submissions for Ones and Zeroes.
// Memory Usage: 9.8 MB, less than 54.89% of C++ online submissions for Ones and Zeroes.

// dp i是0的数量，j是1的数量，dp[i][j]是最多可以使用多少字符串
class Solution {
public:
    int findMaxForm(vector<string>& strs, int m, int n) {
        std::vector<std::vector<int>> dp(m + 1, std::vector<int>(n + 1, 0));
        int zeros, ones;
        for (const std::string& str : strs) {
            zeros = std::count(str.begin(), str.end(), '0');
            ones = str.size() - zeros;
            for (int i = m; i >= zeros; --i) {
                for (int j = n; j >= ones; --j) {
                    dp[i][j] = std::max(dp[i][j], dp[i - zeros][j - ones] + 1);
                }
            }
        }
        return dp[m][n];
    }
};
