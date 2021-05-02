// Runtime: 8 ms, faster than 81.02% of C++ online submissions for License Key Formatting.
// Memory Usage: 8.3 MB, less than 52.17% of C++ online submissions for License Key Formatting.
class Solution {
public:
    string licenseKeyFormatting(string S, int K) {
        string res;
        for (int i = S.size() - 1; i >= 0; --i) {
            if (S[i] != '-') {
                if (res.size() % (K + 1) == K) {
                    res += '-';
                }
                res += std::toupper(S[i]);
            }
        }
        std::reverse(res.begin(), res.end());
        return res;
    }
};
