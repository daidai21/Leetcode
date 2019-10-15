// Runtime: 0 ms, faster than 100.00% of C++ online submissions for First Missing Positive.
// Memory Usage: 8.7 MB, less than 80.00% of C++ online submissions for First Missing Positive.
class Solution {
public:
    int firstMissingPositive(vector<int>& nums) {
        nums.push_back(0);
        int n = nums.size();
        for (int i = 0; i < nums.size(); ++i)
            if (nums[i] < 0 || nums[i] >= n)
                nums[i] = 0;
        for (int i = 0; i < nums.size(); ++i)
            nums[nums[i] % n] += n;
        for (int i = 0; i < nums.size(); ++i) {
            if (nums[i] / n == 0)
                return i;
        }
        return nums.size();
    }
};
