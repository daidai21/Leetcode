// Runtime: 116 ms, faster than 65.43% of C++ online submissions for Find All Numbers Disappeared in an Array.
// Memory Usage: 14.7 MB, less than 100.00% of C++ online submissions for Find All Numbers Disappeared in an Array.
class Solution {
public:
    vector<int> findDisappearedNumbers(vector<int>& nums) {
        vector<int> result;
        for (int num : nums) {
            int idx = abs(num) - 1;
            if (nums[idx] > 0)
                nums[idx] = -nums[idx];
        }
        for (int i = 0; i < nums.size(); ++i)
            if (nums[i] > 0)
                result.push_back(i + 1);
        return result;
    }
};
