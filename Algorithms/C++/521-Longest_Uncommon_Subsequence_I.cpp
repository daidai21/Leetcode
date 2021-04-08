// Runtime: 0 ms, faster than 100.00% of C++ online submissions for Longest Uncommon Subsequence I.
// Memory Usage: 6.1 MB, less than 48.61% of C++ online submissions for Longest Uncommon Subsequence I.
class Solution {
public:
    int findLUSlength(string a, string b) {
        return a == b ? -1 : max(a.size(), b.size());
    }
};
