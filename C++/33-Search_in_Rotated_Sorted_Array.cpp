// Runtime: 4 ms, faster than 82.06% of C++ online submissions for Search in Rotated Sorted Array.
// Memory Usage: 8.8 MB, less than 69.75% of C++ online submissions for Search in Rotated Sorted Array.
class Solution {
public:
    int search(vector<int>& nums, int target) {
        int l = 0, r = nums.size() - 1;
        while (l <= r) {
            int mid = (l + r) / 2;
            if (nums[mid] == target)
                return mid;
            if (nums[mid] >= nums[l]) { // left continue
                if (target >= nums[l] && target < nums[mid])
                    r = mid - 1;
                else
                    l = mid + 1;
            } else { // right continue
                if (target > nums[mid] && target <= nums[r])
                    l = mid + 1;
                else
                    r = mid - 1;
            }
        }
        return -1;
    }
};
