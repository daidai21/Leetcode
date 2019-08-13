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
