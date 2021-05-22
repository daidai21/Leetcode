// Runtime: 12 ms, faster than 6.75% of C++ online submissions for Richest Customer Wealth.
// Memory Usage: 7.9 MB, less than 45.15% of C++ online submissions for Richest Customer Wealth.
#include <numeric>

class Solution {
public:
    int maximumWealth(vector<vector<int>>& accounts) {
        int res = 0;
        for (const std::vector<int>& account : accounts) {
            res = std::max(res, 
                           std::accumulate(account.begin(), account.end(), 0));
        }
        return res;
    }
};
