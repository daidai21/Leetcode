class Solution {
public:
    bool checkZeroOnes(string s) {
        return longestCont(s, '1') > longestCont(s, '0');
    }

private:
    int longestCont(const std::string& s, const char& ch) {
        int res = 0;
        int l = 0, r;
        while (l < s.size()) {
            if (s[l] == ch) {
                r = l;
                while (r < s.size() - 1 && s[r] == s[r + 1]) {
                    r++;
                }
                res = std::max(res, r - l + 1);
                l = r + 1;
            } else {
                l++;
            }
        }
        return res;
    }
};
