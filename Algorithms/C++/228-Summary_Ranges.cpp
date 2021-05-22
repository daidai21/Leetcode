// Runtime: 4 ms, faster than 100.00% of C++ online submissions for Summary Ranges.
// Memory Usage: 6.9 MB, less than 55.49% of C++ online submissions for Summary Ranges.

class Solution {
public:
    vector<string> summaryRanges(vector<int>& nums) {
        if (nums.size() == 0) {
            return {};
        }
        if (nums.size() == 1) {
            return { std::to_string(nums[0]) };
        }
        std::vector<string> res;
        int left = 0, right = 1;
        while (right <= nums.size()) {
            while (right < nums.size() && nums[right] == nums[right - 1] + 1) {
                right++;
            }
            if (left + 1 == right) {
                res.push_back(std::to_string(nums[left]));
            } else {
                res.push_back(std::to_string(nums[left]) + "->" 
                              + std::to_string(nums[right - 1]));
            }
            left = right;
            right++;
        }
        return res;
    }
};
