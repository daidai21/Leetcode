// Runtime: 32 ms, faster than 92.70% of C++ online submissions for Shortest Unsorted Continuous Subarray.
// Memory Usage: 10.4 MB, less than 100.00% of C++ online submissions for Shortest Unsorted Continuous Subarray.
class Solution {
public:
    int findUnsortedSubarray(vector<int>& nums) {
        int l = -1, r = -2, mn = nums[nums.size() - 1], mx = nums[0];
        for (int i = 0; i < nums.size(); ++i) {
            mx = max(mx, nums[i]);
            if (nums[i] < mx)
                r = i;
            mn = min(mn, nums[nums.size() - i - 1]);
            if (mn < nums[nums.size() - i - 1])
                l = nums.size() - i - 1;
        }
        return r - l + 1;
    }
};
