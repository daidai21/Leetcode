// Runtime: 56 ms, faster than 47.29% of C++ online submissions for Interval List Intersections.
// Memory Usage: 16.3 MB, less than 24.00% of C++ online submissions for Interval List Intersections.
class Solution {
public:
    vector<vector<int>> intervalIntersection(vector<vector<int>>& A, vector<vector<int>>& B) {
        vector<vector<int>> res;
        int a = 0, b = 0;
        while (a < A.size() && b < B.size()) {
            int left = max(A[a][0], B[b][0]);
            int right = min(A[a][1], B[b][1]);
            if (left <= right) {
                vector<int> temp = {left, right};
                res.push_back(temp);
            }
            if (A[a][1] < B[b][1])
                ++a;
            else
                ++b;
        }
        return res;
    }
};
