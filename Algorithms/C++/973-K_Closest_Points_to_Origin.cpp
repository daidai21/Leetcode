// Runtime: 296 ms, faster than 34.50% of C++ online submissions for K Closest Points to Origin.
// Memory Usage: 36.9 MB, less than 93.75% of C++ online submissions for K Closest Points to Origin.
class Solution {
public:
    vector<vector<int>> kClosest(vector<vector<int>>& points, int K) {
        sort(points.begin(), points.end(), [](const vector<int>& point1, const vector<int>& point2) {
            return (point1[0] * point1[0] + point1[1] * point1[1])
                < (point2[0] * point2[0] + point2[1] * point2[1]);
        });
        points.resize(K);
        return points;
    }
};
