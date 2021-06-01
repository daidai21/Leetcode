// Runtime: 4 ms, faster than 48.53% of C++ online submissions for Goat Latin.
// Memory Usage: 6.7 MB, less than 33.37% of C++ online submissions for Goat Latin.

class Solution {
public:
    string toGoatLatin(string S) {
        std::string res, word, vowel("aeiouAEIOU");
        int a_cnt = 1, i = 0;
        while (i <= S.size()) {
            if (S[i] == ' ' || i == S.size()) {
                if (vowel.find(word[0]) != std::string::npos) {
                    res += word;
                } else {
                    res += word.substr(1, word.size() - 1) + word[0];
                }
                res += "ma" + std::string(a_cnt, 'a') + " ";
                a_cnt++;
                word = "";
            } else {
                word += S[i];
            }
            i++;
        }
        return res.substr(0, res.size() - 1);
    }
};
