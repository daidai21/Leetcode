// Runtime: 12 ms, faster than 79.19% of C++ online submissions for Relative Ranks.
// Memory Usage: 9.9 MB, less than 84.97% of C++ online submissions for Relative Ranks.
class Solution {
public:
    vector<string> findRelativeRanks(vector<int>& score) {
        vector<int> rank(score.size());
        for (int i = 0; i < score.size(); ++i) {
            rank[i] = i;
        }
        std::sort(rank.begin(), rank.end(), [&](const int& a, const int& b) { return score[a] > score[b]; });
        vector<string> res(score.size());
        for (int i = 0; i < score.size(); ++i) {
            if (i == 0) {
                res[rank[i]] = "Gold Medal";
            } else if (i == 1) {
                res[rank[i]] = "Silver Medal";
            } else if (i == 2) {
                res[rank[i]] = "Bronze Medal";
            } else {
                res[rank[i]] = std::to_string(i + 1);
            }
        }
        return res;
    }
};
