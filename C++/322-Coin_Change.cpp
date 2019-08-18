// Runtime: 48 ms, faster than 65.47% of C++ online submissions for Coin Change.
// Memory Usage: 12.4 MB, less than 94.12% of C++ online submissions for Coin Change.
class Solution {
public:
    int coinChange(vector<int>& coins, int amount) {
        vector<int> dp(amount + 1, amount + 1);
        dp[0] = 0;
        for (int i = 1; i < amount + 1; ++i)
            for (int j = 0; j < coins.size(); ++j)
                if (coins[j] <= i)
                    dp[i] = min(dp[i], dp[i - coins[j]] + 1);
        return dp[amount] > amount ? -1 : dp[amount];
    }
};
