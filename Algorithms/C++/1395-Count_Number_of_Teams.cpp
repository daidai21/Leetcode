// Runtime: 124 ms, faster than 22.16% of C++ online submissions for Count Number of Teams.
// Memory Usage: 7.7 MB, less than 41.46% of C++ online submissions for Count Number of Teams.
class Solution {
public:
    int numTeams(vector<int>& rating) {
        if (rating.size() < 3) {
            return 0;
        }
        int team_num = 0;
        for (int i = 0; i < rating.size(); ++i) {
            for (int j = i + 1; j < rating.size(); ++j) {
                for (int k = j + 1; k < rating.size(); ++k) {
                    if ((rating[i] < rating[j] && rating[j] < rating[k]) ||
                        (rating[i] > rating[j] && rating[j] > rating[k])) {
                        team_num++;
                    }
                }
            }
        }
        return team_num;
    }
};
