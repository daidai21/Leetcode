#include <string>
#include <vector>
using namespace std;


// Runtime: 4 ms, faster than 98.07% of C++ online submissions for String Compression.
// Memory Usage: 9.4 MB, less than 100.00% of C++ online submissions for String Compression.
class Solution {
public:
    int compress(vector<char>& chars) {
        // calc
        vector<char> tmp;
        int cnt = 1;
        char ch = chars[0];
        for (int i = 1; i < chars.size(); ++i) {
            if (chars[i] == ch) {
                cnt++;
            } else {
                tmp.push_back(ch);
                if  (cnt != 1) {
                    for (char c : std::to_string(cnt)) {
                        tmp.push_back(c);
                    }
                }
                ch = chars[i];
                cnt = 1;
            }
        }
        tmp.push_back(ch);
        if (cnt != 1) {
            for (char c : std::to_string(cnt)) {
                tmp.push_back(c);
            }
        }
        // copy
        int res = tmp.size();
        std::copy(tmp.begin(), tmp.begin() + std::min(tmp.size(), chars.size()), chars.begin());
        if (res > chars.size()) {
            for (int i = chars.size(); i < res; ++i) {
                chars.push_back(tmp[i]);
            }
        }
        return res;
    }
};


// Space: O(1)
// Time: O(N)
class Solution {
public:
    int compress(vector<char>& chars) {
        int anchor = 0,
            write = 0;
        for (int read = 0; read < chars.size(); ++read) {
            if (read + 1 == chars.size() || chars[read + 1] != chars[read]) {
                chars[write] = chars[anchor];
                write++;
                if (read > anchor) {
                    for (char c : std::to_string(read - anchor + 1)) {
                        chars[write] = c;
                        write++;
                    }
                }
                anchor = read + 1;
            }
        }
        return write;
    }
};
