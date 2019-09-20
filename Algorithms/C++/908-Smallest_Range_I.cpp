// Runtime: 12 ms, faster than 97.41% of C++ online submissions for Smallest Range I.
// Memory Usage: 9.7 MB, less than 75.00% of C++ online submissions for Smallest Range I.
class Solution {
public:
    int smallestRangeI(vector<int>& A, int K) {
        return max(*max_element(A.begin(), A.end()) - *min_element(A.begin(), A.end()) - 2 * K, 0);
    }
};
