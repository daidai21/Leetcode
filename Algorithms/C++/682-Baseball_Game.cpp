// Runtime: 0 ms, faster than 100.00% of C++ online submissions for Baseball Game.
// Memory Usage: 8.2 MB, less than 93.24% of C++ online submissions for Baseball Game.
// Stack
class Solution {
public:
    int calPoints(vector<string>& ops) {
        int res = 0, score = 0;
        std::vector<int> tmp;
        for (const std::string& s : ops) {
            if (s == "C") {
                res -= tmp.back();
                tmp.pop_back();
                continue;
            }
            if (s == "D") {
                score = tmp.back() * 2;
                res += score;
            } else if (s == "+") {
                score = tmp[tmp.size() - 1] + tmp[tmp.size() - 2];
                res += score;
            } else {
                score = stoi(s);
                res += score;
            }
            tmp.push_back(score);
        }
        return res;
    }
};
