class Solution {
public:
    void sortColors(vector<int>& nums) {
        sort(nums.begin(), nums.end());
    }
};


// Runtime: 0 ms, faster than 100.00% of C++ online submissions for Sort Colors.
// Memory Usage: 8.6 MB, less than 87.72% of C++ online submissions for Sort Colors.
class Solution {
public:
    void sortColors(vector<int>& nums) {
        quick_sort(nums, 0, nums.size() - 1);
    }
private:
    void quick_sort(vector<int>& nums, int l, int r) {
        if (l >= r)
            return;
        int left = l, right = r;
        int flag = nums[l];
        while (left < right) {
            while (left < right && nums[right] >= flag)
                --right;
            if (left < right) {
                nums[left] = nums[right];
                ++left;
            }
            while (left < right && nums[left] <= flag)
                ++left;
            if (left < right) {
                nums[right] = nums[left];
                --right;
            }
            nums[left] = flag;
            quick_sort(nums, l, left - 1);
            quick_sort(nums, left + 1, r);
        }
    }
};
