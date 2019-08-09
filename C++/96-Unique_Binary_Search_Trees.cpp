// Runtime: 0 ms, faster than 100.00% of C++ online submissions for Unique Binary Search Trees.
// Memory Usage: 8.4 MB, less than 54.55% of C++ online submissions for Unique Binary Search Trees.
class Solution {
public:
    int numTrees(int n) {
        vector<int> dp(n + 1);
        dp[0] = 1;
        for (int i = 1; i < n + 1; ++i)
            for (int j = 1; j < i + 1; ++j)
                dp[i] += dp[j - 1] * dp[i - j];
        return dp[n];
    }
};
