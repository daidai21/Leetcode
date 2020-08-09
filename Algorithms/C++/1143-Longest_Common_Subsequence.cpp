// Time Limit Exceeded
#include <algorithm>


class Solution {
public:
    int longestCommonSubsequence(string text1, string text2, int idx1 = 0, int idx2 = 0) {
        if (idx1 >= text1.size() || idx2 >= text2.size()) {
            return 0;
        } else if (text1[idx1] == text2[idx2]) {
            return 1 + this->longestCommonSubsequence(text1, text2, idx1 + 1, idx2 + 1);
        } else {
            return std::max(this->longestCommonSubsequence(text1, text2, idx1 + 1, idx2),
                            this->longestCommonSubsequence(text1, text2, idx1, idx2 + 1));
        }
    }
};
