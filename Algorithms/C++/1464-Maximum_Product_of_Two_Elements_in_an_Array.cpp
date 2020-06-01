// Runtime: 8 ms, faster than 100.00% of C++ online submissions for Maximum Product of Two Elements in an Array.
// Memory Usage: 10 MB, less than 100.00% of C++ online submissions for Maximum Product of Two Elements in an Array.
class Solution {
public:
    int maxProduct(vector<int>& nums) {
        int max_val1 = 0, // best max value
            max_val2 = 0,
            max_idx = 0;  // best max value index
        for (int i = 0; i < nums.size(); ++i) {
            if (max_val1 < nums[i]) {
                max_val1 = nums[i];
                max_idx = i;
            }
        }
        for (int i = 0; i < nums.size(); ++i) {
            if (max_idx != i && max_val2 < nums[i]) {
                max_val2 = nums[i];
            }
        }
        return (max_val1 - 1) * (max_val2 - 1);
    }
};
