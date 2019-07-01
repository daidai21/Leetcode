// Runtime: 4 ms, faster than 64.73% of C++ online submissions for Distribute Candies to People.
// Memory Usage: 8.3 MB, less than 100.00% of C++ online submissions for Distribute Candies to People.
class Solution {
public:
    vector<int> distributeCandies(int candies, int num_people) {
        vector<int> res(num_people);
        for (int i = 0; candies > 0; candies -= ++i) {
            res[i % num_people] += min(i + 1, candies);
        }
        return res;
    }
};