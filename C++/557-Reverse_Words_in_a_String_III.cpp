// Runtime: 24 ms, faster than 57.95% of C++ online submissions for Reverse Words in a String III.
// Memory Usage: 11.8 MB, less than 73.91% of C++ online submissions for Reverse Words in a String III.
class Solution {
public:
    string reverseWords(string s) {
        if (!s.size())
            return s;
        int l = 0, r = 0;
        while (r < s.size() - 1) {
            while (r <= s.size() - 1 && s[r] != ' ')
                ++r;
            int temp = r - 1;
            while (l < temp) {
                swap(s[l], s[temp]);
                ++l;
                --temp;
            }
            l = r + 1;
            ++r;
        }
        return s;
    }
};


// Runtime: 20 ms, faster than 86.11% of C++ online submissions for Reverse Words in a String III.
// Memory Usage: 11.8 MB, less than 91.30% of C++ online submissions for Reverse Words in a String III.
class Solution {
public:
    string reverseWords(string s) {
        if (!s.size())
            return s;
        int l = 0, r = 0;
        while (r <= s.size() - 1) {
            while (r <= s.size() - 1 && s[r] != ' ')
                ++r;
            reverse(s.begin() + l, s.begin() + r);
            l = r + 1;
            ++r;
        }
        return s;
    }
};
