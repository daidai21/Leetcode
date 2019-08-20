// Runtime: 0 ms, faster than 100.00% of C++ online submissions for House Robber.
// Memory Usage: 8.5 MB, less than 98.11% of C++ online submissions for House Robber.
class Solution {
public:
    int rob(vector<int>& nums) {
        int i = 0, j = 0;
        for (int num : nums) {
            int temp = i;
            i = max(i, j);
            j = temp + num;
        }
        return max(i, j);
    }
};
