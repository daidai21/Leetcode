// Runtime: 720 ms, faster than 96.60% of C++ online submissions for Maximum Number of Visible Points.
// Memory Usage: 120.1 MB, less than 5.64% of C++ online submissions for Maximum Number of Visible Points.


#include <cmath>
#include <vector>
#include <algorithm>

using namespace std;

#define PI 3.14159265
#define MARGIN 1e-9

class Solution {
public:
    int visiblePoints(vector<vector<int>>& points, int angle, vector<int>& location) {
        int common = 0;
        std::vector<double> vals;
        for (int i = 0; i < points.size(); ++i) {
            int x = points[i][0] - location[0];
            int y = points[i][1] - location[1];
            if (x == 0 && y == 0) {
                common++;
            } else {
                double A = get_angle(x, y);
                if (A < 0) A += 360;
                vals.emplace_back(A);
            }
        }
        std::sort(vals.begin(), vals.end());
        std::vector<double> a = vals; // TODO: var name
        a.insert(a.begin(), vals.begin(), vals.end());
        for (int i = vals.size(); i < a.size(); ++i) {
            a[i] += 360;
        }
        int res = 0;
        for (int i = 0, j = 0; i < a.size(); ++i) {
            while (j < a.size() && (a[j] - a[i] <= angle + MARGIN))
                ++j;
            res = max(res, j - i);
        }
        return res + common;
    }

    inline double get_angle(int x_diff, int y_diff) {
        return std::atan2(y_diff, x_diff) * 180 / PI;
    }
};
