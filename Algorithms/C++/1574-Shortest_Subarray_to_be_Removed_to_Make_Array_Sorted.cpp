// 1574. Shortest Subarray to be Removed to Make Array Sorted

// Runtime: 120 ms, faster than 82.83% of C++ online submissions for Shortest Subarray to be Removed to Make Array Sorted.
// Memory Usage: 66.9 MB, less than 73.70% of C++ online submissions for Shortest Subarray to be Removed to Make Array Sorted.
class Solution {
public:
    int findLengthOfShortestSubarray(vector<int>& arr) {
        int r = arr.size() - 1;
        for (; r > 0 && arr[r] >= arr[r - 1]; --r);
        int res = r;
        for (int l = 0; l < r && (l == 0 || arr[l - 1] <= arr[l]);++l) {
            while (r < arr.size() && arr[r] < arr[l]) ++r;
            res = min(res, r - l - 1);
        }
        return res;
    }
};
