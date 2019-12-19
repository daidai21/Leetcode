// Runtime: 100 ms, faster than 13.85% of C++ online submissions for Shift 2D Grid.
// Memory Usage: 13.3 MB, less than 100.00% of C++ online submissions for Shift 2D Grid.
class Solution {
public:
    vector<vector<int>> shiftGrid(vector<vector<int>>& grid, int k) {
        k = k % (grid.size() * grid[0].size());
        reverse(grid, 0, grid.size() * grid[0].size() - 1);
        reverse(grid, 0, k - 1);
        reverse(grid, k, grid.size() * grid[0].size() - 1);
        return grid;
    }

private:
    void reverse(vector<vector<int>>& grid, int low, int high) {
        while (low < high) {
            int row = low / grid[0].size(),
                col = low % grid[0].size(),
                i = high / grid[0].size(),
                j = high % grid[0].size();
            swap(grid[row][col], grid[i][j]);
            low++;
            high--;
        }
    }
};
