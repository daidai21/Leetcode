// Runtime: 208 ms, faster than 5.35% of C++ online submissions for Minimum Absolute Difference.
// Memory Usage: 26.3 MB, less than 100.00% of C++ online submissions for Minimum Absolute Difference.
class Solution {
public:
    vector<vector<int>> minimumAbsDifference(vector<int>& arr) {
        int min_diff = INT_MAX;
        sort(arr.begin(), arr.end());
        vector<vector<int>> result;
        for (int i = 1; i < arr.size(); ++i) {
            vector<int> tmp = {arr[i - 1], arr[i]};
            int diff = tmp[1] - tmp[0];
            if (diff < min_diff) {
                result.clear();
                result.push_back(tmp);
            } else if (diff == min_diff) {
                result.push_back(tmp);
            }
            min_diff = min(min_diff, diff);
        }
        return result;
    }
};
