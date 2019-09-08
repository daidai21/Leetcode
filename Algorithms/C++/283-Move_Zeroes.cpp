// Runtime: 20 ms, faster than 23.52% of C++ online submissions for Move Zeroes.
// Memory Usage: 9.3 MB, less than 100.00% of C++ online submissions for Move Zeroes.
class Solution {
public:
    void moveZeroes(vector<int>& nums) {
        int zeroes_times = 0;
        for (int i = nums.size() - 1; i >= 0; --i)
            if (nums[i] == 0) {
                nums.erase(nums.begin() + i);
                ++zeroes_times;
            }
        for (int i = 0; i < zeroes_times; ++i)
            nums.push_back(0);
    }
};
