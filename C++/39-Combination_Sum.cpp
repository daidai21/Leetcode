// Runtime: 8 ms, faster than 98.27% of C++ online submissions for Combination Sum.
// Memory Usage: 9.2 MB, less than 99.01% of C++ online submissions for Combination Sum.
class Solution {
public:
    vector<vector<int>> combinationSum(vector<int>& candidates, int target) {
        sort(candidates.begin(), candidates.end());
        vector<vector<int>> res;
        vector<int> curr;
        recursion(candidates, target, res, curr, 0);
        return res;
    }
private:
    void recursion(vector<int>& candidates, int target, vector<vector<int>>& res, 
                   vector<int>& curr, int idx) {
        if (!target) {
            res.push_back(curr);
            return;
        }
        for (int i = idx; i != candidates.size() && target >= candidates[i]; ++i) {
            curr.push_back(candidates[i]);
            recursion(candidates, target - candidates[i], res, curr, i);
            curr.pop_back();
        }
    }
};
