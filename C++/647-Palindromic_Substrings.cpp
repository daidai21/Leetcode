// Runtime: 4 ms, faster than 90.93% of C++ online submissions for Palindromic Substrings.
// Memory Usage: 8.5 MB, less than 80.00% of C++ online submissions for Palindromic Substrings.
class Solution {
public:
    int countSubstrings(string s) {
        int res = 0, n = s.length();
        for(int i = 0; i < n; ++i){
            for(int j = 0; i - j >= 0 && i + j < n && s[i - j] == s[i + j]; ++j)
                ++res;
            for(int j = 0; i - j - 1 >= 0 && i + j < n && s[i - 1 - j] == s[i + j]; ++j)
                ++res;
        }  
        return res;
    }
};