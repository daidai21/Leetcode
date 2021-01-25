// Runtime: 32 ms, faster than 97.98% of C++ online submissions for Binary Search.
// Memory Usage: 27.6 MB, less than 91.50% of C++ online submissions for Binary Search.
class Solution {
public:
    int search(vector<int>& nums, int target) {
        int l = 0, r = nums.size() - 1, mid = 0;
        while (l <= r) {
            mid = l + (r - l) / 2;
            if (nums[mid] == target) {
                break;
            } else if (nums[mid] > target) {
                r = mid - 1;
            } else if (nums[mid] < target) {
                l = mid + 1;
            }
        }
        return nums[mid] == target ? mid : -1;
    }
};
