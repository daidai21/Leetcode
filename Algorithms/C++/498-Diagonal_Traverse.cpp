// 498. Diagonal Traverse

// Runtime: 20 ms, faster than 99.82% of C++ online submissions for Diagonal Traverse.
// Memory Usage: 18.2 MB, less than 81.83% of C++ online submissions for Diagonal Traverse.

class Solution {
public:
    vector<int> findDiagonalOrder(vector<vector<int>>& matrix) {
        if (matrix.empty()) {
            return {};
        }
        vector<int> res;
        int i = 0,
            j = 0,
            s = 0, // added count
            dire = 1; // 1 is right up, 0 is left down
        while (s < matrix.size() * matrix[0].size()) {
            res.push_back(matrix[i][j]);
            if (dire == 1) {
                if (i - 1 >= 0 && j + 1 < matrix[0].size()) {
                    i--;
                    j++;
                } else if (j + 1 >= matrix[0].size()) {
                    dire = 0;
                    i++;
                } else if (i - 1 < 0) {
                    dire = 0;
                    j++;
                }
            } else if (dire == 0) {
                if (i + 1 < matrix.size() && j - 1 >= 0) {
                    i++;
                    j--;
                } else if (i + 1 >= matrix.size()) {
                    j++;
                    dire = 1;
                } else if (j - 1 < 0) {
                    i++;
                    dire = 1;
                }
            }
            s++;
        }
        return res;
    }
};
