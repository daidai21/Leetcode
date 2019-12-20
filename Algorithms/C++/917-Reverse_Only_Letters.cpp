// Runtime: 0 ms, faster than 100.00% of C++ online submissions for Reverse Only Letters.
// Memory Usage: 8.7 MB, less than 9.09% of C++ online submissions for Reverse Only Letters.
class Solution {
public:
    string reverseOnlyLetters(string S) {
        stack<char> stk;
        string result;
        for (char ch : S)
            if (isalpha(ch))
                stk.push(ch);
        for (char ch : S)
            if (isalpha(ch)) {
                result.push_back(stk.top());
                stk.pop();
            } else
                result.push_back(ch);
        return result;
    }
};
