// Time Limit Exceeded
class Solution {
public:
    int maxProduct(vector<int>& nums) {
        if (nums.empty())
            return 0;
        int res = INT_MIN;
        for (int i = 0; i < nums.size(); ++i)
            for (int j = i; j < nums.size(); ++j) {
                int tmp = nums[i];
                for (int z = i + 1; z <= j; ++z)
                    tmp *= nums[z];
                res = max(res, tmp);
            }
        return res;
    }
};


// Runtime: 312 ms, faster than 5.16% of C++ online submissions for Maximum Product Subarray.
// Memory Usage: 9.2 MB, less than 60.00% of C++ online submissions for Maximum Product Subarray.
class Solution {
public:
    int maxProduct(vector<int>& nums) {
        if (nums.empty())
            return 0;
        int res = INT_MIN;
        for (int i = 0; i < nums.size(); ++i) {
            for (int j = i, tmp = 1; j < nums.size(); ++j) {
                tmp *= nums[j];
                res = max(res, tmp);
            }
        }
        return res;
    }
};


// Runtime: 4 ms, faster than 89.30% of C++ online submissions for Maximum Product Subarray.
// Memory Usage: 9.2 MB, less than 50.00% of C++ online submissions for Maximum Product Subarray.
class Solution {
public:
    int maxProduct(vector<int>& nums) {
        if (nums.empty())
            return 0;
        int res = INT_MIN, pre_max = 1, pre_min = 1;
        for (int n : nums) {
            if (n < 0)
                swap(pre_max, pre_min);
            pre_max = max(pre_max * n, n);
            pre_min = min(pre_min * n, n);
            res = max(res, pre_max);
        }
        return res;
    }
};
