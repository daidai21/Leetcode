// Runtime: 0 ms, faster than 100.00% of C++ online submissions for Target Sum.
// Memory Usage: 8.5 MB, less than 76.92% of C++ online submissions for Target Sum.
class Solution {
public:
    int findTargetSumWays(vector<int>& nums, int S) {
        int sum = accumulate(nums.begin(), nums.end(), 0);
        if (sum < S || (sum + S) & 1)
            return 0;
        // dp
        S = (S + sum) >> 1;
        vector<int> dp(S + 1, 0);
        dp[0] = 1;
        for (int n : nums)
            for (int i = S; i >= n; --i)
                dp[i] += dp[i - n];
        return dp[S];
    }
};
