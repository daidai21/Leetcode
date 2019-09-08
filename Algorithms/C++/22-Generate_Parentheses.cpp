// Runtime: 8 ms, faster than 59.82% of C++ online submissions for Generate Parentheses.
// Memory Usage: 17.4 MB, less than 30.33% of C++ online submissions for Generate Parentheses.
class Solution {
public:
    vector<string> generateParenthesis(int n) {
        recursion(n, 0, 0, "");
        return res;
    }
private:
    vector<string> res;
    void recursion(int n, int l, int r, string curr) {
        if (l == n && r == n) {
            res.push_back(curr);
            return;
        }
        if (l < n)
            recursion(n, l + 1, r, curr + '(');
        if (r < n && r < l)
            recursion(n, l, r + 1, curr + ')');
    }
};
