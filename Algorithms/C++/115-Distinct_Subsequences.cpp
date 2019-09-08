// Runtime: 8 ms, faster than 72.60% of C++ online submissions for Distinct Subsequences.
// Memory Usage: 14.7 MB, less than 41.67% of C++ online submissions for Distinct Subsequences.
class Solution {
public:
    int numDistinct(string s, string t) {
        vector<vector<long int>> dp(t.size() + 1, vector<long int>(s.size() + 1));
        for (int j = 0; j < s.size() + 1; ++j)
            dp[0][j] = 1;
        for (int i = 1; i < t.size() + 1; ++i)
            for (int j = 1; j < s.size() + 1; ++j)
                dp[i][j] = dp[i][j - 1] + (t[i - 1] == s[j - 1] ? dp[i - 1][j - 1] : 0);
        return dp[t.size()][s.size()];
    }
};
