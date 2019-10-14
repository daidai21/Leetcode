// Runtime: 40 ms, faster than 82.80% of C++ online submissions for Product of Array Except Self.
// Memory Usage: 12.4 MB, less than 98.48% of C++ online submissions for Product of Array Except Self.
class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        vector<int> res(nums.size(), 0);
        res[0] = 1;
        for (int i = 1; i < nums.size(); ++i)
            res[i] = nums[i - 1] * res[i - 1];
        int tmp = 1;
        for (int i = nums.size() - 1; i >= 0; --i) {
            res[i] *= tmp;
            tmp *= nums[i];
        }
        return res;
    }
};
