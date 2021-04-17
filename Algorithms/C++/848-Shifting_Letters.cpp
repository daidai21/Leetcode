// 848. Shifting Letters


// Runtime: 40 ms, faster than 15.00% of C++ online submissions for Shifting Letters.
// Memory Usage: 19.8 MB, less than 84.00% of C++ online submissions for Shifting Letters.
class Solution {
public:
    string shiftingLetters(string S, vector<int>& shifts) {
        for (int i = shifts.size() - 2; i >= 0; --i) {
            shifts[i] = (shifts[i] + shifts[i + 1]) % 26;
        }
        for (int i = 0; i < S.size(); ++i) {
            S[i] = (S[i] - 'a' + shifts[i]) % 26 + 'a';
        }
        return S;
    }
};
