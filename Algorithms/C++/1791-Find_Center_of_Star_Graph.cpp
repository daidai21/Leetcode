// 1791. Find Center of Star Graph


// Runtime: 156 ms, faster than 99.31% of C++ online submissions for Find Center of Star Graph.
// Memory Usage: 67.1 MB, less than 97.21% of C++ online submissions for Find Center of Star Graph.
class Solution {
public:
    int findCenter(vector<vector<int>>& edges) {
        return edges[0][0] == edges[1][0] || edges[0][0] == edges[1][1] ? edges[0][0] : edges[0][1];   
    }
};
