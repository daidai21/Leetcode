// Runtime: 4 ms, faster than 70.71% of C++ online submissions for Remove Element.
// Memory Usage: 8.5 MB, less than 97.06% of C++ online submissions for Remove Element.
class Solution {
public:
    int removeElement(vector<int>& nums, int val) {
        int j = 0;
        for (int i = 0; i < nums.size(); ++i)
            if (nums[i] != val) {
                nums[j] = nums[i];
                ++j;
            }
        return j;
    }
};
