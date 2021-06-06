class Solution {
public:
    bool findRotation(vector<vector<int>>& mat, vector<vector<int>>& target) {
        // 原地
        if (check(mat, target)) return true;
        // 顺时针旋转90
        rotate90(mat);
        if (check(mat, target)) return true;
        // 顺时针旋转180
        rotate90(mat);
        if (check(mat, target)) return true;
        // 顺时针旋转270
        rotate90(mat);
        if (check(mat, target)) return true;
        return false;
    }

    // 顺时针
    void rotate90(vector<vector<int>>& mat) {
        int n = mat.size();
        // 水平翻转
        for (int i = 0; i < n / 2; ++i) {
            for (int j = 0; j < n; ++j) {
                std::swap(mat[i][j], mat[n - i - 1][j]);
            }
        }
        // 主对角线翻转 左上到右下
        for (int i = 0; i < n; ++i) {
            for (int j = 0; j < i; ++j) {
                std::swap(mat[i][j], mat[j][i]);
            }
        }
        return ;
    }
    
    bool check(const vector<vector<int>>& mat, const vector<vector<int>>& target) {
        for (int i = 0; i < mat.size(); ++i) {
            for (int j = 0; j < mat[0].size(); ++j) {
                if (mat[i][j] != target[i][j]) {
                    return false;
                }
            }
        }
        return true;
    }
};

