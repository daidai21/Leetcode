// Runtime: 136 ms, faster than 13.79% of C++ online submissions for Queue Reconstruction by Height.
// Memory Usage: 25.6 MB, less than 11.60% of C++ online submissions for Queue Reconstruction by Height.
class Solution {
public:
    vector<vector<int>> reconstructQueue(vector<vector<int>>& people) {
        sort(people.begin(), people.end(), [](vector<int> p1, vector<int> p2){
            return p1[0] > p2[0] || (p1[0] == p2[0] && p1[1] < p2[1]);
        });
        vector<vector<int>> res;
        for (vector<int> person : people)
            res.insert(res.begin() + person[1], person);
        return res;
    }
};
