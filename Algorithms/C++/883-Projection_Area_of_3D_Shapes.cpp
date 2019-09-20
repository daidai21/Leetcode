// Runtime: 4 ms, faster than 98.88% of C++ online submissions for Projection Area of 3D Shapes.
// Memory Usage: 9.1 MB, less than 100.00% of C++ online submissions for Projection Area of 3D Shapes.
class Solution {
public:
    int projectionArea(vector<vector<int>>& grid) {
        int area = 0;
        for (vector<int>& i : grid) // over look
            for (int& j : i)
                area += j != 0;
        for (vector<int>& i : grid) // left look
            area += *max_element(i.begin(), i.end());
        for (int col = 0; col < grid.size(); ++col) {
            int high = 0;
            for (int row = 0; row < grid.size(); ++row)
                high = max(high, grid[row][col]);
            area += high;
        }
        return area;
    }
};
