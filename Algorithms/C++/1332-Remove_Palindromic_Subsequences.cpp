// 1332. Remove Palindromic Subsequences


// 重点是删除子序列不是子字符串
// Runtime: 0 ms, faster than 100.00% of C++ online submissions for Remove Palindromic Subsequences.
// Memory Usage: 6.2 MB, less than 46.65% of C++ online submissions for Remove Palindromic Subsequences.
class Solution {
public:
    int removePalindromeSub(string s) {
        if (s.empty()) return 0;
        for (int i = 0; i < s.size() / 2; ++i) {
            if (s[i] != s[s.size() - i - 1]) return 2;
        }
        return 1;
    }
};
