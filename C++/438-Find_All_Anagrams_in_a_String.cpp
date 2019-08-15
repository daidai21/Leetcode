// Runtime: 32 ms, faster than 76.32% of C++ online submissions for Find All Anagrams in a String.
// Memory Usage: 10.3 MB, less than 90.38% of C++ online submissions for Find All Anagrams in a String.
class Solution {
public:
    vector<int> findAnagrams(string s, string p) {
        vector<int> sv(26, 0), pv(26, 0), res;
        if (s.size() < p.size())
            return res;
        for (int i = 0; i < p.size(); ++i) {
            ++sv[s[i] - 'a'];
            ++pv[p[i] - 'a'];
        }
        if (sv == pv)
            res.push_back(0);
        for (int i = p.size(); i < s.size(); ++i) {
            ++sv[s[i] - 'a'];
            --sv[s[i - p.size()] - 'a'];
            if (sv == pv)
                res.push_back(i - p.size() + 1);
        }
        return res;
    }
};
