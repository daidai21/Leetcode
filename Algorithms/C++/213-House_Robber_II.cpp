// Runtime: 0 ms, faster than 100.00% of C++ online submissions for House Robber II.
// Memory Usage: 7.7 MB, less than 84.51% of C++ online submissions for House Robber II.
class Solution {
public:
    int rob(vector<int>& nums) {
        if (nums.size() == 1) {
            return nums[0];
        }
        if (nums.size() == 2) {
            return max(nums[0], nums[1]);
        }
        return max(dp(nums, 0, nums.size() - 1), dp(nums, 1, nums.size()));
    }
    
    int dp(const vector<int>& nums, int start, int end) {
        int cur = 0,
            pre = 0,
            tmp;
        for (int i = start; i < end; ++i) {
            tmp = max(nums[i] + pre, cur);
            pre = cur;
            cur = tmp;
        }
        return cur;
    }
};
