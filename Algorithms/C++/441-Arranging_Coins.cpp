// Runtime: 24 ms, faster than 15.97% of C++ online submissions for Arranging Coins.
// Memory Usage: 8.2 MB, less than 100.00% of C++ online submissions for Arranging Coins.
class Solution {
public:
    int arrangeCoins(int n) {
        int cnt = 0,
            i = 1;
        while (n - i >= 0) {
            cnt++;
            n -= i;
            i++;
        }
        return cnt;
    }
};
