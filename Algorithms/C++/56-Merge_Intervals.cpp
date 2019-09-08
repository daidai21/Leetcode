// Runtime: 76 ms, faster than 15.81% of C++ online submissions for Merge Intervals.
// Memory Usage: 28.3 MB, less than 5.17% of C++ online submissions for Merge Intervals.
class Solution {
public:
    vector<vector<int>> merge(vector<vector<int>>& intervals) {
        sort(intervals.begin(), intervals.end(), [](vector<int> it1, vector<int> it2) {
            return it1[0] < it2[0] || (it1[0] == it2[0] && it1[1] < it2[1]);
        });
        vector<vector<int>> res;
        for (vector<int> line : intervals)
            if (res.size() > 0 && line[0] <= res[res.size() - 1][1])
                res[res.size() - 1][1] = max(res[res.size() - 1][1], line[1]);
            else
                res.push_back(line);
        return res;
    }
};
