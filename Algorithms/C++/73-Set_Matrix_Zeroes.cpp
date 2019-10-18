// Runtime: 56 ms, faster than 8.49% of C++ online submissions for Set Matrix Zeroes.
// Memory Usage: 11.4 MB, less than 100.00% of C++ online submissions for Set Matrix Zeroes.
// FIXME:-1000000 as flag is error
class Solution {
public:
    void setZeroes(vector<vector<int>>& matrix) {
        for (int i = 0; i < matrix.size(); ++i)
            for (int j = 0; j < matrix[0].size(); ++j)
                if (matrix[i][j] == 0) {
                    for (int k = 0; k < matrix[0].size(); ++k) // cur row
                        if (matrix[i][k] != 0)
                            matrix[i][k] = -1000000;
                    for (int k = 0; k < matrix.size(); ++k) // cur col
                        if (matrix[k][j] != 0)
                            matrix[k][j] = -1000000;
                }
        for (int i = 0; i < matrix.size(); ++i)
            for (int j = 0; j < matrix[0].size(); ++j)
                if (matrix[i][j] == -1000000)
                    matrix[i][j] = 0;
    }
};
