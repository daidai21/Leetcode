// Runtime: 4 ms, faster than 86.35% of C++ online submissions for Kids With the Greatest Number of Candies.
// Memory Usage: 9.1 MB, less than 49.77% of C++ online submissions for Kids With the Greatest Number of Candies.
class Solution {
public:
    vector<bool> kidsWithCandies(vector<int>& candies, int extraCandies) {
        vector<bool> res(candies.size());
        int max_candies = *std::max_element(candies.begin(), candies.end());
        for (int i = 0; i < candies.size(); ++i) {
            res[i] = candies[i] + extraCandies >= max_candies;
        }
        return res;
    }
};
