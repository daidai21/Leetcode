// Runtime: 0 ms, faster than 100.00% of C++ online submissions for Spiral Matrix.
// Memory Usage: 8.6 MB, less than 63.77% of C++ online submissions for Spiral Matrix.
class Solution {
public:
    vector<int> spiralOrder(vector<vector<int>>& matrix) {
        vector<int> res;
        int row_size = matrix.size();
        if (row_size == 0) return res;
        int col_size = matrix[0].size();
        int left = 0, right = col_size - 1, up = 0, down = row_size - 1;
        int direction = 0, col = 0, row = 0;
        while (left <= right && up <= down) {
            res.push_back(matrix[row][col]);
            switch (direction) {
                case 0:  // right
                    if(col >= right) {
                        direction = 1;
                        row++;
                        up++;
                    } else {
                        col++;
                    }
                    break;
                case 1:  // down
                    if (row >= down) {
                        direction = 2;
                        col--;
                        right--;
                    } else {
                        row++;
                    }
                    break;
                case 2:  // left
                    if (col <= left) {
                        direction = 3;
                        row--;
                        down--;
                    } else {
                        col--;
                    }
                    break;
                default:  // up
                    if (row <= up) {
                        direction = 0;
                        col++;
                        left++;
                    } else {
                        row--;
                    }
            }
        }
        return res;
    }
};
