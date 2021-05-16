// Runtime: 56 ms, faster than 48.72% of C++ online submissions for Find All Duplicates in an Array.
// Memory Usage: 33.7 MB, less than 40.00% of C++ online submissions for Find All Duplicates in an Array.
// 用负数标记

// #include <cmath>
class Solution {
public:
    vector<int> findDuplicates(vector<int>& nums) {
        int tmp;
        std::vector<int> res;
        for (int i = 0; i < nums.size(); ++i) {
            if (nums[std::abs(nums[i]) - 1] < 0) res.push_back(std::abs(nums[i]));
            else nums[std::abs(nums[i]) - 1] = -nums[std::abs(nums[i]) - 1];
        }
        return res;
    }
};
