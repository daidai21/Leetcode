// Runtime: 0 ms, faster than 100.00% of C++ online submissions for Length of Last Word.
// Memory Usage: 8.8 MB, less than 55.56% of C++ online submissions for Length of Last Word.
class Solution {
public:
    int lengthOfLastWord(string s) {
        if (s.size() == 0)
            return 0;
        int j = s.size() - 1;
        while (s[j] == ' ' && j >= 0)
            --j;
        if (j == -1) // all s is space
            return 0;
        int i = j - 1;
        while (s[i] != ' ' && i >= 0)
            --i;
        return j - i;
    }
};
