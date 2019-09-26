class Solution {
public:
    string longestCommonPrefix(vector<string>& strs) {
        string prefix;
        if (strs.size() == 0)
            return prefix;
        bool is_same = true;
        for (int i = 0; i < strs[0].size() && is_same == true; ++i) {
            for (int j = 1; j < strs.size(); ++j)
                if (strs[j - 1][i] != strs[j][i]) {
                    is_same = false;
                    break;
                }
            if (!is_same)
                break;
            prefix += strs[0][i];
        }
        return prefix;
    }
};
