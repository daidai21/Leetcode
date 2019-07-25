class Solution {
public:
    bool isMatch(string s, string p) {
        int s_size = s.size(), p_size = p.size();
        vector<vector<bool>> dp(s_size + 1, vector<bool>(p_size + 1, false));
        dp[0][0] = true;
        for (int col = 1; col < p_size + 1; ++col)
            if (p[col - 1] == '*' && col >= 2)
                dp[0][col] = dp[0][col - 2];
        for (int row = 1; row < s_size + 1; ++row) {
            for (int col = 1; col < p_size + 1; ++col) {
                if (p[col - 1] == '*')
                    dp[row][col] = dp[row][col - 2] || (dp[row - 1][col] && (p[col - 2] == s[row - 1] || p[col - 2] == '.'));
                else
                    dp[row][col] = (p[col - 1] == s[row - 1] || p[col - 1] == '.') && dp[row - 1][col - 1];
            }
        }
        return dp[s_size][p_size];
    }
};
