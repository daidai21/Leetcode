// Runtime: 12 ms, faster than 40.00% of C++ online submissions for Minimum Time Visiting All Points.
// Memory Usage: 10.1 MB, less than 100.00% of C++ online submissions for Minimum Time Visiting All Points.
class Solution {
public:
    int minTimeToVisitAllPoints(vector<vector<int>>& points) {
        int ans = 0;
        for (int i = 1; i < points.size(); ++i)
            ans += max(abs(points[i][0] - points[i - 1][0]), abs(points[i][1] - points[i - 1][1]));
        return ans;
    }
};
