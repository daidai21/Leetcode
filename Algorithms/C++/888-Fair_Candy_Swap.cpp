// Runtime: 88 ms, faster than 75.71% of C++ online submissions for Fair Candy Swap.
// Memory Usage: 48.2 MB, less than 45.39% of C++ online submissions for Fair Candy Swap.
class Solution {
public:
    vector<int> fairCandySwap(vector<int>& A, vector<int>& B) {
        int diff = (std::accumulate(A.begin(), A.end(), 0) - std::accumulate(B.begin(), B.end(), 0)) / 2;
        std::unordered_set<int> st(A.begin(), A.end());
        for (int b : B) if (st.count(b + diff)) return { b + diff, b };
        return {};
    }
};
