// Runtime: 12 ms, faster than 88.32% of C++ online submissions for Basic Calculator.
// Memory Usage: 10.3 MB, less than 100.00% of C++ online submissions for Basic Calculator.
class Solution {
public:
    int calculate(string s) {
        int res = 0;
        stack<int> stac;
        long int num = 0;
        int sign = 1;
        for (char c : s) {
            if ('0' <= c && c <= '9')
                num = num * 10 + c - '0';
            else if (c == '+') {
                res += sign * num;
                sign = 1;
                num = 0;
            } else if (c == '-') {
                res += sign * num;
                sign = -1;
                num = 0;
            } else if (c == '(') {
                stac.push(res);
                stac.push(sign);
                sign = 1;
                res = 0;
            } else if (c == ')') {
                res += sign * num;
                res *= stac.top();
                stac.pop();
                res += stac.top();
                stac.pop();
                num = 0;
            }
        }
        return res + sign * num;
    }
};
