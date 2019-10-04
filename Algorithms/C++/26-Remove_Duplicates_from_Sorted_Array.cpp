// Runtime: 20 ms, faster than 93.27% of C++ online submissions for Remove Duplicates from Sorted Array.
// Memory Usage: 9.8 MB, less than 97.50% of C++ online submissions for Remove Duplicates from Sorted Array.
class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        if (nums.size() == 0)
            return 0;
        int i = 0;
        for (int j = 1; j < nums.size(); ++j)
            if (nums[i] != nums[j]) {
                ++i;
                nums[i] = nums[j];
            }
        return i + 1;
    }
};
