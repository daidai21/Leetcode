// Runtime: 0 ms, faster than 100.00% of C++ online submissions for Decode String.
// Memory Usage: 8.8 MB, less than 94.12% of C++ online submissions for Decode String.
class Solution {
public:
    string decodeString(string s) {
        stack<string> stack1;
        stack<int> stack2;
        string res;
        int num = 0;
        for (char ch : s) {
            if (ch == '[') {
                stack1.push(res);
                stack2.push(num);
                res = "";
                num = 0;
            } else if (ch == ']') {
                string temp = res;
                for (int i = 0; i < stack2.top() - 1; ++i)
                    res += temp;
                res = stack1.top() + res;
                stack2.pop();
                stack1.pop();
            } else if (isdigit(ch)) {
                num = num * 10 + (ch - '0');
            } else {
                res.push_back(ch);
            }
        }
        return res;
    }
};
