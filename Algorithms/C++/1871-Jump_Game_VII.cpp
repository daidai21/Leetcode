// pre 表示我们可以从其跳到的上一个位置的数量
// DP
class Solution {
public:
    bool canReach(string s, int minJump, int maxJump) {
        int pre = 0;
        std::vector<bool> dp(s.size(), false);
        dp[0] = true;
        for (int i = 1; i < s.size(); ++i) {
            if (i >= minJump) {
                pre += dp[i - minJump];
            }
            if (i > maxJump) {
                pre -= dp[i - maxJump - 1];
            }
            dp[i] = pre > 0 && s[i] == '0';
        }
        return dp[s.size() - 1];
    }
};
