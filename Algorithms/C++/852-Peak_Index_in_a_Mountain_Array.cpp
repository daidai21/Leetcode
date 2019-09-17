// Runtime: 0 ms, faster than 100.00% of C++ online submissions for Peak Index in a Mountain Array.
// Memory Usage: 9.4 MB, less than 71.43% of C++ online submissions for Peak Index in a Mountain Array.
class Solution {
public:
    int peakIndexInMountainArray(vector<int>& A) {
        return distance(begin(A), max_element(A.begin(), A.end()));
    }
};
