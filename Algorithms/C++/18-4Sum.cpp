// Runtime: 992 ms, faster than 5.02% of C++ online submissions for 4Sum.
// Memory Usage: 9.3 MB, less than 75.44% of C++ online submissions for 4Sum.
class Solution {
public:
    vector<vector<int>> fourSum(vector<int>& nums, int target) {
        vector<vector<int>> res;
        sort(nums.begin(), nums.end());
        for (int a = 0; a < nums.size(); ++a)
            for (int b = a + 1; b < nums.size(); ++b)
                for (int c = b + 1; c < nums.size(); ++c)
                    for (int d = c + 1; d < nums.size(); ++d)
                        if (nums[a] + nums[b] + nums[c] + nums[d] == target) {
                            vector<int> tmp = {nums[a], nums[b], nums[c], nums[d]};
                            if (find(res.begin(), res.end(), tmp) == res.end())
                                res.push_back(tmp);
                        }
        return res;
    }
};
