class Solution {
public:
    vector<bool> checkArithmeticSubarrays(vector<int>& nums, vector<int>& l, vector<int>& r) {
        vector<bool> res;
        for (int i = 0; i < l.size(); ++i) {
            vector<int> tmp(nums.begin() + l[i], nums.begin() + r[i] + 1);
            sort(tmp.begin(), tmp.end());
            res.push_back(is_arithmetic_subarray(tmp));
        }
        return res;
    }
    
    bool is_arithmetic_subarray(const vector<int>& tmp) {
        // for (auto i : tmp) cout << i << " "; cout << endl;
        int diff;
        for (int i = 0; i < tmp.size() - 1; ++i) {
            if (i == 0) {
                diff = tmp[i] - tmp[i + 1];
            } else if (diff != tmp[i] - tmp[i + 1]) {
                return false;
            }
        }
        return true;
    }
};
