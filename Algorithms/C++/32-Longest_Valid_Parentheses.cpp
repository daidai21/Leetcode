class Solution {
public:
    int longestValidParentheses(string s) {
        int left = 0, right = 0, maxLen = 0;
        for (int i = 0; i < s.size(); ++i) { // left -> right scan
            s[i] == '(' ? left++ : right++;
            if (left == right) {
                maxLen = std::max(maxLen, 2 * right);
            } else if (right >= left) {
                left = 0;
                right = 0;
            }
        }
        left = 0;
        right = 0;
        for (int i = s.size() - 1; i >= 0; --i) { // right -> left scan
            s[i] == '(' ? left++ : right++;
            if (left == right) {
                maxLen = std::max(maxLen, 2 * left);
            } else if (left >= right) {
                left = 0;
                right = 0;
            }
        }
        return maxLen;
    }
};
