// 1749. Maximum Absolute Sum of Any Subarray


// Kadane算法
// 最大子数列问题
// 
// Runtime: 60 ms, faster than 66.09% of C++ online submissions for Maximum Absolute Sum of Any Subarray.
// Memory Usage: 41.5 MB, less than 32.75% of C++ online submissions for Maximum Absolute Sum of Any Subarray.
class Solution {
public:
    int maxAbsoluteSum(vector<int>& nums) {
        int res = 0, mi = 0, ma = 0;
        for (const int& n : nums) {
            mi = min(0, mi + n);
            ma = max(0, ma + n);
            res = max(res, max(ma, -mi));
        }
        return res;
    }
};
