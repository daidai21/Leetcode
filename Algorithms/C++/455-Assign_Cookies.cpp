// 455. Assign Cookies

// Runtime: 28 ms, faster than 60.27% of C++ online submissions for Assign Cookies.
// Memory Usage: 17.5 MB, less than 17.11% of C++ online submissions for Assign Cookies.
class Solution {
public:
    int findContentChildren(vector<int>& g, vector<int>& s) {
        sort(g.begin(), g.end());
        sort(s.begin(), s.end());
        int res = 0;
        for (int i = 0, j = 0; i < g.size(); ++i) {
            while (j < s.size() && s[j] < g[i]) ++j;
            if (j >= s.size()) break;
            if (g[i] <= s[j]) {
                res++;
                j++;
            }
        }
        return res;
    }
};


// Runtime: 24 ms, faster than 87.43% of C++ online submissions for Assign Cookies.
// Memory Usage: 17.5 MB, less than 62.08% of C++ online submissions for Assign Cookies.
class Solution {
public:
    int findContentChildren(vector<int>& g, vector<int>& s) {
        sort(g.begin(), g.end());
        sort(s.begin(), s.end());
        int res = 0;
        for (int j = 0; res < g.size() && j < s.size(); ++j) {
            if (g[res] <= s[j]) res++;
        }
        return res;
    }
};
