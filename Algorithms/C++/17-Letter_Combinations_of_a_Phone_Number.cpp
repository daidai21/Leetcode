// Runtime: 4 ms, faster than 59.36% of C++ online submissions for Letter Combinations of a Phone Number.
// Memory Usage: 8.7 MB, less than 71.43% of C++ online submissions for Letter Combinations of a Phone Number.
class Solution {
public:
    vector<string> letterCombinations(string digits) {
        vector<string> res;
        return recursion(digits, res);
    }
private:
    vector<string> phone = {"", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"};
    vector<string> recursion(string digits, vector<string> cur) {
        if (digits.size() == 0)
            return cur;
        vector<string> next;
        int number = digits[0] - '0';
        if (cur.size() == 0)
            for (char c : phone[number])
                next.push_back(string(1, c));
        else
            for (char c : phone[number])
                for (string s : cur)
                    next.push_back(s + c);
        return recursion(digits.substr(1, digits.size()), next);
    }
};
