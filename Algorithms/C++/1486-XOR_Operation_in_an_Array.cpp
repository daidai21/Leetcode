// Runtime: 0 ms, faster than 100.00% of C++ online submissions for XOR Operation in an Array.
// Memory Usage: 6.1 MB, less than 41.61% of C++ online submissions for XOR Operation in an Array.
class Solution {
public:
    int xorOperation(int n, int start) {
        int res = start;
        for (int i = 1; i < n; ++i) {
            res = res ^ (start + i * 2);
        }
        return res;
    }
};
