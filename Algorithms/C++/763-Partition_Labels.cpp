// Runtime: 4 ms, faster than 97.41% of C++ online submissions for Partition Labels.
// Memory Usage: 6.6 MB, less than 100.00% of C++ online submissions for Partition Labels.
class Solution {
public:
    vector<int> partitionLabels(string S) {
        vector<int> hp(26, 0); // HashMap: max(index)
        for (int i = 0; i < S.size(); ++i) {
            hp[S[i] - 'a'] = max(hp[S[i] - 'a'], i);
        }
        int j = 0, z = 0;
        vector<int> res;
        for (int i = 0; i < S.size(); ++i) {
            j = max(j, hp[S[i] - 'a']);
            if (i == j) {
                res.push_back(i - z + 1);
                z = i + 1;
            }
        }
        return res;
    }
};
