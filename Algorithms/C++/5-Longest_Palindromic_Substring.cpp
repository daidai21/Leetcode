class Solution {
private:
    int s_size;
    string palindrome(string s, int left, int right) {
        while (left >= 0 && right < s_size && s[left] == s[right]) {
            --left;
            ++right;
        }
        return s.substr(left + 1, right - left - 1);
    }
public:
    string longestPalindrome(string s) {
        s_size = s.size();
        string res = "", tmp = "";
        for (int i = 0; i < s_size; ++i) {
            tmp = palindrome(s, i, i);
            if (tmp.size() > res.size())
                res.swap(tmp);
            tmp = palindrome(s, i, i + 1);
            if (tmp.size() > res.size())
                res.swap(tmp);
        }
        return res;
    }
};


// Runtime: 4 ms, faster than 98.49% of C++ online submissions for Longest Palindromic Substring.
// Memory Usage: 8.6 MB, less than 94.84% of C++ online submissions for Longest Palindromic Substring.
class Solution {
public:
    string longestPalindrome(string s) {
        if (s.empty())
            return "";
        if (s.size() == 1)
            return s;
        int min_start = 0, max_len = 1;
        for (int i = 0; i < s.size(); ) {
            if (s.size() - i <= max_len / 2)
                break;
            int j = i, k = i;
            while (k < s.size() - 1 && s[k + 1] == s[k]) // skip duplicate characters
                ++k;
            i = k + 1; // update i
            while (k < s.size() - 1 && j > 0 && s[k + 1] == s[j - 1]) { // expand
                ++k;
                --j;
            }
            int new_len = k - j + 1;
            if (new_len > max_len) {
                min_start = j;
                max_len = new_len;
            }
        }
        return s.substr(min_start, max_len);
    }
};



class Solution {
public:
    string longestPalindrome(string s) {
        if (s.size() < 2) return s;
        std::string res = "", tmp;
        for (int i = 0; i < s.size(); ++i) {
            tmp = expandAroundCenter(s, i, i);
            if (tmp.size() > res.size()) res = tmp;
            tmp = expandAroundCenter(s, i, i + 1);
            if (tmp.size() > res.size()) res = tmp;
        }
        return res;
    }

private:
    std::string expandAroundCenter(const std::string& s, int l, int r) {
        while (l >= 0 && r < s.size() && s[l] == s[r]) {
            l--;
            r++;
        }
        return s.substr(l + 1, r - l - 1);
    }
};
