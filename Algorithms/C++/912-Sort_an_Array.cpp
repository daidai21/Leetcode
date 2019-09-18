// Runtime: 64 ms, faster than 65.21% of C++ online submissions for Sort an Array.
// Memory Usage: 12.5 MB, less than 97.22% of C++ online submissions for Sort an Array.
class Solution {
public:
    vector<int> sortArray(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        return nums;
    }
};
