// Runtime: 8 ms, faster than 78.88% of C++ online submissions for Redundant Connection.
// Memory Usage: 9.9 MB, less than 76.47% of C++ online submissions for Redundant Connection.
class Solution {
public:
    vector<int> findRedundantConnection(vector<vector<int>>& edges) {
        vector<int> root(edges.size() + 1, -1);
        for (vector<int> edge : edges) {
            int x = find(root, edge[0]);
            int y = find(root, edge[1]);
            if (x == y)
                return edge;
            root[x] = y;
        }
        vector<int> res = {-1, -1};
        return res;
    }

    int find(const vector<int>& root, int x) {
        while (root[x] != -1)
            x = root[x];
        return x;
    }
};
