// Runtime: 44 ms, faster than 17.80% of C++ online submissions for DI String Match.
// Memory Usage: 10.2 MB, less than 42.86% of C++ online submissions for DI String Match.
class Solution {
public:
    vector<int> diStringMatch(string S) {
        vector<int> A;
        int low = 0, high = S.size();
        for (char s : S)
            if (s == 'I')
                A.push_back(low++);
            else
                A.push_back(high--);
        A.push_back(high);
        return A;
    }
};
