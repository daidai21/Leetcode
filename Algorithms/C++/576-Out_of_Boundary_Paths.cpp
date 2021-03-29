// 576. Out of Boundary Paths

// Time Limit Exceeded
class Solution {
public:
    int findPaths(int m, int n, int N, int i, int j) {
        if (i == m || j == n || i < 0 || j < 0) return 1;
        if (N == 0) return 0;
        return findPaths(m, n, N - 1, i - 1, j)
            + findPaths(m, n, N - 1, i + 1, j)
            + findPaths(m, n, N - 1, i, j - 1)
            + findPaths(m, n, N - 1, i, j + 1);
    }
};


// Recursion with Memoization
// Runtime: 8 ms, faster than 75.40% of C++ online submissions for Out of Boundary Paths.
// Memory Usage: 9.3 MB, less than 41.58% of C++ online submissions for Out of Boundary Paths.
class Solution {
public:
    int findPaths(int m, int n, int N, int i, int j) {
        vector<vector<vector<int>>> mem(m, vector<vector<int>>(n, vector<int>(N + 1, -1)));
        return findPaths(m, n, N, i, j, mem);
    }

private:
    int findPaths(int m, int n, int N, int i, int j, vector<vector<vector<int>>>& mem) {
        if (i == m || j == n || i < 0 || j < 0) return 1;
        if (N == 0) return 0;
        if (mem[i][j][N] >= 0) return mem[i][j][N];
        mem[i][j][N] = (
            (findPaths(m, n, N - 1, i + 1, j, mem) + findPaths(m, n, N - 1, i - 1, j, mem)) % M + 
            (findPaths(m, n, N - 1, i, j + 1, mem) + findPaths(m, n, N - 1, i, j - 1, mem)) % M
        ) % M;
        return mem[i][j][N];
    }

    int M = 1000000007;
};
