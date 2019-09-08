// Runtime: 4 ms, faster than 99.04% of C++ online submissions for Next Permutation.
// Memory Usage: 8.5 MB, less than 93.16% of C++ online submissions for Next Permutation.
class Solution {
public:
    void nextPermutation(vector<int>& nums) {
        int idx = nums.size() - 1;
        while (idx > 0 && nums[idx - 1] >= nums[idx])
            --idx;
        if (idx == 0)
            sort(nums.begin(), nums.end());
        else {
            for (int i = nums.size() - 1; i > idx - 1; --i) {
                if (nums[i] > nums[idx - 1]) {
                    swap(nums[i], nums[idx - 1]);
                    break;
                }
            }
            sort(nums.begin() + idx, nums.end());
        }
    }
};


// Runtime: 4 ms, faster than 99.04% of C++ online submissions for Next Permutation.
// Memory Usage: 8.7 MB, less than 55.56% of C++ online submissions for Next Permutation.
class Solution {
public:
    void nextPermutation(vector<int>& nums) {
        next_permutation(nums.begin(), nums.end());
    }
};
