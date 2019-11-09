// Runtime: 4 ms, faster than 56.44% of C++ online submissions for Hamming Distance.
// Memory Usage: 8.3 MB, less than 40.91% of C++ online submissions for Hamming Distance.
class Solution {
public:
    int hammingDistance(int x, int y) {
        int cnt = 0, num = x ^ y;
        while (num > 0) {
            cnt += num & 1;
            num >>= 1;
        }
        return cnt;
    }
};
