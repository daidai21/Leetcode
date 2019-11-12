// brute force
// Runtime: 548 ms, faster than 7.32% of C++ online submissions for Find K Pairs with Smallest Sums.
// Memory Usage: 118.3 MB, less than 20.00% of C++ online submissions for Find K Pairs with Smallest Sums.
class Solution {
public:
    vector<vector<int>> kSmallestPairs(vector<int>& nums1, vector<int>& nums2, int k) {
        vector<vector<int>> ans;
        for (int n1 : nums1)
            for (int n2 : nums2) {
                vector<int> tmp = {n1, n2};
                ans.push_back(tmp);
            }
        sort(ans.begin(), ans.end(), [](const vector<int>& num1, const vector<int>& num2) {
            return num1[0] + num1[1] < num2[0] + num2[1];
        });
        if (ans.size() <= k)
            return ans;
        ans.erase(ans.begin() + k, ans.end());
        return ans;
    }
};
