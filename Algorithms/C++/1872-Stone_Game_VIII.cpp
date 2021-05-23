// Runtime: 148 ms, faster than 75.00% of C++ online submissions for Stone Game VIII.
// Memory Usage: 87.3 MB, less than 75.00% of C++ online submissions for Stone Game VIII.
class Solution {
public:
    int stoneGameVIII(vector<int>& stones) {
        std::vector<int> sm(stones.size() + 1, 0);
        for (int i = 0; i < stones.size(); ++i) sm[i + 1] = sm[i] + stones[i];
        int res = sm[stones.size()];
        for (int i = stones.size() - 1; i >= 2; --i) res = std::max(res, sm[i] - res);
        return res;
    }
};
