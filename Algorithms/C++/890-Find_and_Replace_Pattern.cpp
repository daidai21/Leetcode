// Runtime: 4 ms, faster than 76.96% of C++ online submissions for Find and Replace Pattern.
// Memory Usage: 8.6 MB, less than 42.28% of C++ online submissions for Find and Replace Pattern.
class Solution {
public:
    vector<string> findAndReplacePattern(vector<string>& words, string pattern) {
        std::vector<std::string> res;
        for (const std::string& word : words) {
            if (match(word, pattern)) res.push_back(word);
        }
        return res;
    }
    
private:
    bool match(std::string word, std::string pattern) {
        std::map<char, char> m1;
        std::map<char, char> m2;
        char w, p;
        for (int i = 0; i < word.length(); ++i) {
            w = word[i];
            p = pattern[i];
            if (m1.find(w) == m1.end()) m1[w] = p;
            if (m2.find(p) == m2.end()) m2[p] = w;
            if (m1[w] != p || m2[p] != w) return false;
        }
        return true;
    }
};
