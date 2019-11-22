// Runtime: 12 ms, faster than 9.24% of C++ online submissions for Buddy Strings.
// Memory Usage: 9.1 MB, less than 87.50% of C++ online submissions for Buddy Strings.
class Solution {
public:
    bool buddyStrings(string A, string B) {
        if (A.size() != B.size())
            return false;
        if (A == B) {
            set<char> seen;
            for (char a : A) {
                if (seen.find(a) != seen.end())
                    return true;
                seen.insert(a);
            }
            return false;
        } else {
            vector<pair<char, char>> diff;
            for (int i = 0; i < A.size(); ++i) {
                if (A[i] != B[i])
                    diff.push_back(make_pair(A[i], B[i]));
                if (diff.size() > 2)
                    return false;
            }
            return diff.size() == 2 && diff[0].first == diff[1].second && diff[0].second == diff[1].first;
        }
    }
};
