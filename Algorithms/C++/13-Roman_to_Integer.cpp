// Runtime: 28 ms, faster than 13.11% of C++ online submissions for Roman to Integer.
// Memory Usage: 10.6 MB, less than 22.55% of C++ online submissions for Roman to Integer.
class Solution {
public:
    int romanToInt(string s) {
        map<char, int> sym_val = {
            {'I', 1},
            {'V', 5},
            {'X', 10},
            {'L', 50},
            {'C', 100},
            {'D', 500},
            {'M', 1000},
        };
        int result = sym_val[s[s.size() - 1]];
        for (int i = s.size() - 2; i >= 0; --i) {
            if (sym_val[s[i]] < sym_val[s[i + 1]])
                result -= sym_val[s[i]];
            else
                result += sym_val[s[i]];
        }
        return result;
    }
};
