// Runtime: 12 ms, faster than 5.37% of C++ online submissions for Longest Palindrome.
// Memory Usage: 10.5 MB, less than 6.67% of C++ online submissions for Longest Palindrome.
class Solution {
public:
    int longestPalindrome(string s) {
        set<int> se;
        for (char c : s)
            if (se.find(c) == se.end())
                se.insert(c);
            else
                se.erase(c);
        return se.size() > 0 ? s.size() - se.size() + 1 : s.size();
    }
};
