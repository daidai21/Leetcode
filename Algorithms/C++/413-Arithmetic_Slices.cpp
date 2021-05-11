// Runtime: 4 ms, faster than 61.31% of C++ online submissions for Arithmetic Slices.
// Memory Usage: 7.2 MB, less than 98.89% of C++ online submissions for Arithmetic Slices.
// DP

class Solution {
public:
    int numberOfArithmeticSlices(vector<int>& nums) {
        int cur = 0, add = 0;
        for (int i = 2; i < nums.size(); ++i) {
            if (nums[i] - nums[i - 1] == nums[i - 1] - nums[i - 2]) {
                cur++;
                add += cur;
            } else {
                cur = 0;
            }
        }
        return add;
    }
};
