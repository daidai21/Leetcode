// Runtime: 4 ms, faster than 97.80% of C++ online submissions for Subsets.
// Memory Usage: 17.9 MB, less than 6.78% of C++ online submissions for Subsets.
class Solution {
public:
    vector<vector<int>> subsets(vector<int>& nums) {
        vector<vector<int>> res;
        vector<int> temp;
        recursion(res, temp, nums, 0);
        return res;
    }
private:
    void recursion(vector<vector<int>>& res, vector<int> temp, 
                   vector<int>& nums, int idx) {
        if (idx >= nums.size()) {
            res.push_back(temp);
            return;
        }
        recursion(res, temp, nums, idx + 1);
        temp.push_back(nums[idx]);
        recursion(res, temp, nums, idx + 1);
    }
};
