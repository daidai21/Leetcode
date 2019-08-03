// Runtime: 40 ms, faster than 79.31% of C++ online submissions for Group Anagrams.
// Memory Usage: 19.8 MB, less than 51.17% of C++ online submissions for Group Anagrams.
class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        unordered_map<string, vector<string>> dic;
        for (string str : strs) {
            string tmp = str;
            sort(tmp.begin(), tmp.end());
            dic[tmp].push_back(str);
        }
        vector<vector<string>> res;
        for (auto kv : dic)
            res.push_back(kv.second);
        return res;
    }
};
