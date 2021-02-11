// Runtime: 4 ms, faster than 98.83% of C++ online submissions for Minimum Size Subarray Sum.
// Memory Usage: 10.7 MB, less than 53.15% of C++ online submissions for Minimum Size Subarray Sum.

#include <climits>

class Solution {
public:
    int minSubArrayLen(int target, vector<int>& nums) {
        int res = INT_MAX;
        int left = 0;
        int sum = 0;
        for (int right = 0; right < nums.size(); ++right) {
            sum += nums[right];
            while (sum >= target) {
                res = min(res, right + 1 - left);
                sum -= nums[left];
                left++;
            }
        }
        return res != INT_MAX ? res : 0;
    }
};
