// Runtime: 0 ms, faster than 100.00% of C++ online submissions for Get Maximum in Generated Array.
// Memory Usage: 6.3 MB, less than 33.00% of C++ online submissions for Get Maximum in Generated Array.

class Solution {
public:
    int getMaximumGenerated(int n) {
        vector<int> tab(n + 2);
        tab[1] = 1;
        if (n <= 1) return tab[n];
        int res = 0;
        for (int i = 2; i <= n; ++i) {
            if (i % 2 == 0) {
                tab[i] = tab[i / 2];
            } else {
                tab[i] = tab[i / 2] + tab[i / 2 + 1];
            }
            res = max(res, tab[i]);
        }
        return res;
    }
};
