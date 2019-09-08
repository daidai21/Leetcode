// Runtime: 4 ms, faster than 49.45% of C++ online submissions for Rectangle Overlap.
// Memory Usage: 8.1 MB, less than 100.00% of C++ online submissions for Rectangle Overlap.
class Solution {
public:
    bool isRectangleOverlap(vector<int>& rec1, vector<int>& rec2) {
        return rec1[0] < rec2[2] && rec2[0] < rec1[2] && rec1[1] < rec2[3] && rec2[1] < rec1[3];
    }
};
