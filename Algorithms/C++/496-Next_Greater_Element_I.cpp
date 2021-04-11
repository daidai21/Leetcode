// 496. Next Greater Element I


// Runtime: 24 ms, faster than 8.55% of C++ online submissions for Next Greater Element I.
// Memory Usage: 8.4 MB, less than 94.03% of C++ online submissions for Next Greater Element I.
class Solution {
public:
    vector<int> nextGreaterElement(vector<int>& nums1, vector<int>& nums2) {
        vector<int> res(nums1.size(), -1);
        for (int i = 0; i < nums1.size(); ++i) {
            bool found = false;
            for (int j = 0; j < nums2.size(); ++j) {
                if (nums1[i] == nums2[j]) {
                    found = true;
                } else if (found == true && nums1[i] < nums2[j]) {
                    res[i] = nums2[j];
                    break;
                }
            }
        }
        return res;
    }
};



// Time: O(N)
// Space: O(N)
// Runtime: 8 ms, faster than 54.02% of C++ online submissions for Next Greater Element I.
// Memory Usage: 8.9 MB, less than 54.64% of C++ online submissions for Next Greater Element I.
class Solution {
public:
    vector<int> nextGreaterElement(vector<int>& nums1, vector<int>& nums2) {
        stack<int> stk;
        unordered_map<int, int> mp;
        for (int n : nums2) {
            while (stk.size() && n > stk.top()) {
                mp[stk.top()] = n;
                stk.pop();
            }
            stk.push(n);
        }
        vector<int> res;
        for (int n : nums1) {
            res.push_back( mp.count(n) ? mp[n] : -1);
        }
        return res;
    }
};
