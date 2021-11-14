// Runtime: 200 ms, faster than 5.58% of C++ online submissions for Kth Largest Element in an Array.
// Memory Usage: 9 MB, less than 100.00% of C++ online submissions for Kth Largest Element in an Array.
class Solution {
public:
    int findKthLargest(vector<int>& nums, int k) {
        for (int i = 0; i < k - 1; ++i) {
            vector<int>::iterator it = max_element(nums.begin(), nums.end());
            *it = INT_MIN;
        }
        return *max_element(nums.begin(), nums.end());
    }
};


class Solution {
public:
    int findKthLargest(vector<int>& nums, int k) {
        int left = 0, right = nums.size() - 1;
        while (true) {
            // 快排
            int i = left, j = right;
            int idx = std::rand() % (right - left + 1) + left;
            std::swap(nums[left], nums[idx]);
            while (i < j) {
                while (i < j && nums[j] >= nums[left]) --j;
                while (i < j && nums[i] <= nums[left]) ++i;
                std::swap(nums[i], nums[j]);
            }
            std::swap(nums[i], nums[left]);
            // 新增逻辑
            if (i == nums.size() - k) return nums[i]; // 若恰为倒数第K的位置
            else if (i > nums.size() - k) right = i - 1; // 将查找范围放在该位置左侧
            else left = i + 1; // 将查找范围放在该位置右侧
        }
    }
};
