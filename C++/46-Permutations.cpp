// Runtime: 12 ms, faster than 71.03% of C++ online submissions for Permutations.
// Memory Usage: 9.1 MB, less than 98.08% of C++ online submissions for Permutations.
class Solution {
public:
    vector<vector<int>> permute(vector<int>& nums) {
        vector<vector<int>> res;
        recursion(nums, 0, res);
        return res;
    }
private:
    void recursion(vector<int>& nums, int begin, vector<vector<int>>& res) {
        if (begin >= nums.size()) {
            res.push_back(nums);
            return;
        }
        for (int i = begin; i < nums.size(); ++i) {
            swap(nums[begin], nums[i]);
            recursion(nums, begin + 1, res);
            swap(nums[begin], nums[i]);
        }
    }
};
