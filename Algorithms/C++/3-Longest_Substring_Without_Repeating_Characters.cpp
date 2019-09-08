// Runtime: 8 ms, faster than 95.93% of C++ online submissions for Longest Substring Without Repeating Characters.
// Memory Usage: 10.4 MB, less than 67.18% of C++ online submissions for Longest Substring Without Repeating Characters.
class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        vector<int> dic(256, -1);
        int max_len = 0, start = -1;
        for (int i = 0; i != s.length(); ++i) {
            if (dic[s[i]] > start)
                start = dic[s[i]];
            dic[s[i]] = i;
            max_len = max(max_len, i - start);
        }
        return max_len;
    }
};
