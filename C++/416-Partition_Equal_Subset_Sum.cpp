// Runtime: 148 ms, faster than 37.45% of C++ online submissions for Partition Equal Subset Sum.
// Memory Usage: 8.4 MB, less than 82.35% of C++ online submissions for Partition Equal Subset Sum.
class Solution {
public:
    bool canPartition(vector<int>& nums) {
        int sum_half = accumulate(nums.begin(), nums.end(), 0);
        if (sum_half & 1)
            return false;
        else
            sum_half /= 2;
        vector<bool> dp(sum_half + 1);
        dp[0] = true;
        for (int num : nums)
            for (int i = sum_half; i >= num; --i)
                dp[i] = dp[i] || dp[i - num];
        return dp[sum_half];
    }
};
