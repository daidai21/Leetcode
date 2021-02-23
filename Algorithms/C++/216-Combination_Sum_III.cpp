// Runtime: 0 ms, faster than 100.00% of C++ online submissions for Combination Sum III.
// Memory Usage: 6.2 MB, less than 98.47% of C++ online submissions for Combination Sum III.
class Solution {
public:
    vector<vector<int>> combinationSum3(int k, int n) {
        vector<vector<int>> res;
        vector<int> cur;
        back_tracking(res, k, n, 1, cur);
        return res;
    }
    
    void back_tracking(vector<vector<int>>& res, int k, int n, int level, vector<int>& curr) {
        if (n < 0) {
            return ;
        }
        if (n == 0 && k == 0) {
            res.push_back(curr);
        }
        for (int i = level; i <= 9; ++i) {
            curr.push_back(i);
            back_tracking(res, k - 1, n - i, i + 1, curr);
            curr.pop_back();
        }
    }
};
