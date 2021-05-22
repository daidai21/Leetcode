// Runtime: 116 ms, faster than 7.06% of C++ online submissions for Count Items Matching a Rule.
// Memory Usage: 31 MB, less than 34.24% of C++ online submissions for Count Items Matching a Rule.

class Solution {
public:
    int countMatches(vector<vector<string>>& items, string ruleKey, string ruleValue) {
        int res = 0;
        for (const std::vector<string>& item : items) {
            if (ruleKey == "type") {
                res += item[0] == ruleValue;
            } else if (ruleKey == "color") {
                res += item[1] == ruleValue;
            } else if (ruleKey == "name") {
                res += item[2] == ruleValue;
            }
        }
        return res;
    }
};
