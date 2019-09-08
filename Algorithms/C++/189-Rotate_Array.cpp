// Runtime: 12 ms, faster than 99.67% of C++ online submissions for Rotate Array.
// Memory Usage: 9.4 MB, less than 85.41% of C++ online submissions for Rotate Array.
class Solution {
public:
    void rotate(vector<int>& nums, int k) {
        int n = nums.size();
        k %= n;
        if (k == 0) return;
        reverse_(nums, 0, n - 1);
        reverse_(nums, 0, k - 1);
        reverse_(nums, k, n - 1);
    }
private:
    void reverse_(vector<int> &nums, int start, int end) {
        int tmp;
        while (start < end) {
            tmp = nums[start];
            nums[start] = nums[end];
            nums[end] = tmp;
            start++;
            end--;
        }
    }
};