// Runtime: 1048 ms, faster than 5.05% of C++ online submissions for Search a 2D Matrix II.
// Memory Usage: 12.7 MB, less than 100.00% of C++ online submissions for Search a 2D Matrix II.
class Solution {
public:
    bool searchMatrix(vector<vector<int>>& matrix, int target) {
        for (int i = 0; i < matrix.size(); ++i)
            for (int j = 0; j < matrix[0].size(); ++j)
                if (matrix[i][j] == target)
                    return true;
        return false;
    }
};


// Runtime: 72 ms, faster than 56.09% of C++ online submissions for Search a 2D Matrix II.
// Memory Usage: 12.7 MB, less than 100.00% of C++ online submissions for Search a 2D Matrix II.
class Solution {
public:
    bool searchMatrix(vector<vector<int>>& matrix, int target) {
        int row = matrix.size() - 1, col = 0;
        while (row >= 0 && col < matrix[0].size()) {
            if (matrix[row][col] == target)
                return true;
            else if (matrix[row][col] > target)
                --row;
            else
                ++col;
        }
        return false;
    }
};
