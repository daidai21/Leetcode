// Runtime: 28 ms, faster than 66.93% of C++ online submissions for Candy.
// Memory Usage: 10.6 MB, less than 30.77% of C++ online submissions for Candy.
class Solution {
public:
    int candy(vector<int>& ratings) {
        vector<int> candys(ratings.size(), 1);
        for (int i = 1; i < ratings.size(); ++i)
            if (ratings[i] > ratings[i - 1])
                candys[i] = candys[i - 1] + 1;
            else
                candys[i] = 1;
        for (int i = ratings.size() - 2; i >= 0; --i)
            if (ratings[i] > ratings[i + 1])
                candys[i] = max(candys[i], candys[i + 1] + 1);
        return accumulate(candys.begin(), candys.end(), 0);
    }
};
