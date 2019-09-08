// Runtime: 0 ms, faster than 100.00% of C++ online submissions for Valid Parentheses.
// Memory Usage: 8.6 MB, less than 22.12% of C++ online submissions for Valid Parentheses.
class Solution {
public:
    bool isValid(string s) {
        stack<char> stk;
        for (char c : s) {
            switch(c) {
                case '(':
                    stk.push(')');
                    break;
                case '{':
                    stk.push('}');
                    break;
                case '[':
                    stk.push(']');
                    break;
                default:
                    if (stk.size() == 0 || c != stk.top())
                        return false;
                    else
                        stk.pop();
            }
        }
        return stk.size() == 0;
    }
};