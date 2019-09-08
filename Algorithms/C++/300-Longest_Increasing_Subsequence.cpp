// Runtime: 40 ms, faster than 45.37% of C++ online submissions for Longest Increasing Subsequence.
// Memory Usage: 8.6 MB, less than 93.75% of C++ online submissions for Longest Increasing Subsequence.
class Solution {
public:
    int lengthOfLIS(vector<int>& nums) {
        if (nums.size() < 2)
            return nums.size();
        vector<int> dp(nums.size() + 1, 1);
        for (int i = 0; i < nums.size(); ++i)
            for (int j = 0; j < i; ++j)
                if (nums[i] > nums[j])
                    dp[i] = max(dp[i], dp[j] + 1);
        return *max_element(dp.begin(), dp.end());
    }
};
