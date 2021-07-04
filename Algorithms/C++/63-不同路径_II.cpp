// dp
class Solution {
public:
    int uniquePathsWithObstacles(vector<vector<int>>& obstacleGrid) {
        if (obstacleGrid[0][0] == 1) return 0;
        obstacleGrid[0][0] = 1;
        for (int i = 1; i < obstacleGrid[0].size(); ++i) { // fill first row
            obstacleGrid[0][i] = (obstacleGrid[0][i] == 0 && obstacleGrid[0][i - 1] == 1) ? 1 : 0;
        }
        for (int i = 1; i < obstacleGrid.size(); ++i) { // fill first col
            obstacleGrid[i][0] = (obstacleGrid[i][0] == 0 && obstacleGrid[i - 1][0] == 1) ? 1 : 0;
        }
        for (int i = 1; i < obstacleGrid.size(); ++i) {
            for (int j = 1; j < obstacleGrid[0].size(); ++j) {
                obstacleGrid[i][j] = (obstacleGrid[i][j] == 0) ? (obstacleGrid[i][j - 1] + obstacleGrid[i - 1][j]) : 0;
            }
        }
        return obstacleGrid[obstacleGrid.size() - 1][obstacleGrid[0].size() - 1];
    }
};
