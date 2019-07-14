// Runtime: 788 ms, faster than 5.01% of C++ online submissions for Maximum Subarray.
// Memory Usage: 9.3 MB, less than 34.42% of C++ online submissions for Maximum Subarray.
class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        vector<int> pre_vec(nums.size() + 1);
        pre_vec[0] = 0;
        int res = nums[0];
        for (int i = 1; i < pre_vec.size() ; ++i)
            pre_vec[i] = pre_vec[i - 1] + nums[i - 1];
        for (int start = 0; start < nums.size() + 1; ++start)
            for (int end = start + 1; end < nums.size() + 1; ++end)
                res = max(res, pre_vec[end] - pre_vec[start]);
        return res;
    }
};


class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        int res = INT_MIN, tmp = 0;
        for (int num : nums) {
            tmp += num;
            res = max(res, tmp);
            if (tmp < 0)
                tmp = 0;
        }
        return res;
    }
};
