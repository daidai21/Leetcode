// Runtime: 8 ms, faster than 92.05% of C++ online submissions for Wildcard Matching.
// Memory Usage: 8.9 MB, less than 76.92% of C++ online submissions for Wildcard Matching.
class Solution {
public:
    bool isMatch(string s, string p) {
        int i = 0, j = 0, asterisk = -1, match;
        while (i < s.size()) {
            if (j < p.size() && p[j] == '*') {
                match = i; 
                asterisk = j++;
            } else if (j < p.size() && (s[i] == p[j] || p[j] == '?')) {
                i++; 
                j++;
            } else if (asterisk >= 0) {
                i = ++match;
                j = asterisk + 1;
            } else
                return false;
        }
        while (j < p.size() && p[j] == '*')
            j++;
        return j == p.size();
    }
};
