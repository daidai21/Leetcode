class Solution {
public:
    int minimumEffortPath(vector<vector<int>>& heights) {
        // binary search
        int low = 0,
            high = 1000000;
        while (low < high) {
            int mid = low + (high - low) / 2;
            if (is_path(heights, mid)) {
                high = mid;
            } else {
                low = mid + 1;
            }
        }
        return low;
    }
    
    // bfs
    bool is_path(const vector<vector<int>>& heights, int effort) {
        int N = heights.size(),
            M = heights[0].size();
        vector<bool> flag(N * M, false); // visited
        flag[0] = true;
        queue<int> que; // route
        que.push(0);
        vector<vector<int>> dir = {
            {0, 1},
            {1, 0},
            {-1, 0},
            {0, -1}
        };
        while (!que.empty()) {
            int pos = que.front();
            que.pop();
            int x = pos / M,
                y = pos % M;
            for (int i = 0; i < dir.size(); ++i) {
                int nx = x + dir[i][0],
                    ny = y + dir[i][1];
                if (nx < 0 || nx >= N || ny < 0 || ny >= M)
                    continue;
                if (abs(heights[nx][ny] - heights[x][y]) > effort)
                    continue;
                int npos = nx * M + ny;
                if (flag[npos])
                    continue;
                flag[npos] = true;
                que.push(npos);
            }
        }
        return flag[N * M - 1];
    }
};
