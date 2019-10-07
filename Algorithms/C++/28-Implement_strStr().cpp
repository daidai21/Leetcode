// Runtime: 8 ms, faster than 47.98% of C++ online submissions for Implement strStr().
// Memory Usage: 9.3 MB, less than 32.86% of C++ online submissions for Implement strStr().
class Solution {
public:
    int strStr(string haystack, string needle) {
        if (!needle.size())
            return 0;
        if (haystack.size() < needle.size()) // some time haystack.size() - needle.size() < 0
            return -1;
        for (int i = 0; i < haystack.size() - needle.size() + 1; ++i) {
            if (haystack.substr(i, needle.size()) == needle)
                return i;
        }
        return -1;
    }
};
