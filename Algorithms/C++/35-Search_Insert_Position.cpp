// Runtime: 4 ms, faster than 98.20% of C++ online submissions for Search Insert Position.
// Memory Usage: 9 MB, less than 43.75% of C++ online submissions for Search Insert Position.
class Solution {
public:
    int searchInsert(vector<int>& nums, int target) {
        int i = 0;
        while (i < nums.size() && nums[i] < target)
            ++i;
        return i;
    }
};
