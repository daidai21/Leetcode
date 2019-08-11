// Runtime: 8 ms, faster than 77.07% of C++ online submissions for Word Break.
// Memory Usage: 12 MB, less than 60.38% of C++ online submissions for Word Break.
class Solution {
public:
    bool wordBreak(string s, vector<string>& wordDict) {
        vector<bool> dp(s.size() + 1, false);
        dp[0] = true;
        for (int i = 0; i < s.size(); ++i) {
            for (int j = i; j >= 0; --j) {
                string temp = s.substr(j, i - j + 1);
                if (dp[j])
                    if (find(wordDict.begin(), wordDict.end(), temp) != wordDict.end()) {
                        dp[i + 1] = true;
                        break;
                    }
            }
        }
        return dp[s.size()];
    }
};
