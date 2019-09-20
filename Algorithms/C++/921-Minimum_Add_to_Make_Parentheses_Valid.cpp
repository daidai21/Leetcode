// Runtime: 4 ms, faster than 58.46% of C++ online submissions for Minimum Add to Make Parentheses Valid.
// Memory Usage: 8.4 MB, less than 84.62% of C++ online submissions for Minimum Add to Make Parentheses Valid.
class Solution {
public:
    int minAddToMakeValid(string S) {
        int left_brackets = 0,
            min_add = 0;
        for (char s : S) {
            if (s == '(')
                ++left_brackets;
            else
                --left_brackets;
            if (left_brackets < 0) {
                min_add += 0 - left_brackets;
                left_brackets = 0;
            }
        }
        return min_add + left_brackets;
    }
};
