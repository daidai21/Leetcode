// 递归 递归深度搜索
// Runtime: 36 ms, faster than 33.98% of C++ online submissions for Max Area of Island.
// Memory Usage: 35.4 MB, less than 6.66% of C++ online submissions for Max Area of Island.
class Solution {
public:
    int maxAreaOfIsland(vector<vector<int>>& grid) {
        int res = 0;
        for (int i = 0; i < grid.size(); ++i) {
            for (int j = 0; j < grid[0].size(); ++j) {
                res = max(res, area(grid, i, j));
            }
        }
        return res;
    }
    
    int area(const vector<vector<int>>& grid, int row, int col) {
        if (!(0 <= row && row < grid.size() &&
             0 <= col && col < grid[0].size() &&
             seen.find(std::make_pair(row, col)) == seen.end() &&
             grid[row][col] == 1)) {
            return 0;
        }
        seen.insert(std::make_pair(row, col));
        return (1 + 
               area(grid, row + 1, col) +
               area(grid, row - 1, col) +
               area(grid, row, col + 1) +
               area(grid, row, col - 1));
    }
    
private:
    std::set<std::pair<int, int>> seen;
};
