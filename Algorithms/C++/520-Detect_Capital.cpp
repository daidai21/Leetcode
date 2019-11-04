// Runtime: 0 ms, faster than 100.00% of C++ online submissions for Detect Capital.
// Memory Usage: 8.2 MB, less than 50.00% of C++ online submissions for Detect Capital.
class Solution {
public:
    bool detectCapitalUse(string word) {
        if (word.size() == 1)
            return true;
        int upper_num = 0;
        for (int i = 1; i < word.size(); ++i)
            if (isupper(word[i]))
                upper_num++;
        return upper_num == 0 || (isupper(word[0]) && upper_num == word.size() - 1);
    }
};


// Runtime: 8 ms, faster than 59.77% of C++ online submissions for Detect Capital.
// Memory Usage: 8.2 MB, less than 75.00% of C++ online submissions for Detect Capital.
class Solution {
public:
    bool detectCapitalUse(string word) {
        for (int i = 1; i < word.size(); ++i)
            if (isupper(word[1]) != isupper(word[i]) || islower(word[0]) && isupper(word[i]))
                return false;
        return true;
    }
};
