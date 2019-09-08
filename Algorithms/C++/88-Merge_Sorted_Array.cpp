class Solution {
public:
    void merge(vector<int>& nums1, int m, vector<int>& nums2, int n) {
        for (int i : nums2) {
            nums1[m] = i;
            m++;
        }
        sort(nums1.begin(), nums1.end());
    }
};