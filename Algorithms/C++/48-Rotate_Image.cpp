// Runtime: 4 ms, faster than 83.81% of C++ online submissions for Rotate Image.
// Memory Usage: 8.9 MB, less than 100.00% of C++ online submissions for Rotate Image.
class Solution {
public:
    void rotate(vector<vector<int>>& matrix) {
        int tmp;
        for (int i = 0; i < matrix.size(); ++i)
            for (int j = 0; j < matrix[0].size(); ++j)
                if (i > j) {
                    tmp = matrix[i][j];
                    matrix[i][j] = matrix[j][i];
                    matrix[j][i] = tmp;
                }
        for (vector<int>& line : matrix)
            reverse(line.begin(), line.end());
    }
};
