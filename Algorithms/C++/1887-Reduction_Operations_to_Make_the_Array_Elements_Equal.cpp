class Solution {
public:
    int reductionOperations(vector<int>& nums) {
        if (nums.size() == 1) return 0;
        std::sort(nums.begin(), nums.end());
        int res = 0, step = 0;
        for (int i = 1; i < nums.size(); ++i) {
            step += nums[i] != nums[i - 1];
            res += step;
        }
        return res;
    }
};
