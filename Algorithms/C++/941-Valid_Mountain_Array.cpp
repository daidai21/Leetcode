// 941. Valid Mountain Array

// Runtime: 32 ms, faster than 25.11% of C++ online submissions for Valid Mountain Array.
// Memory Usage: 22.5 MB, less than 37.99% of C++ online submissions for Valid Mountain Array.
class Solution {
public:
    bool validMountainArray(vector<int>& arr) {
        if (arr.size() < 3) return false;
        int max_idx = 0;
        for (; max_idx < arr.size(); ++max_idx) {
            // max val in front
            if (max_idx == 0 && arr[max_idx] >= arr[max_idx + 1]) {
                return false;
            } else if (arr[max_idx] > arr[max_idx + 1]) {
                break;
            // val same
            } else if (arr[max_idx] == arr[max_idx + 1]) {
                return false;
            }
        }
        // max val in end
        if (max_idx == arr.size() - 1) return false;
        for (; max_idx < arr.size() - 1; ++max_idx) {
            if (arr[max_idx] <= arr[max_idx + 1]) return false;
        }
        return true;
    }
};


// Runtime: 20 ms, faster than 96.65% of C++ online submissions for Valid Mountain Array.
// Memory Usage: 22.4 MB, less than 37.99% of C++ online submissions for Valid Mountain Array.
class Solution {
public:
    bool validMountainArray(vector<int>& arr) {
        int i = 0;
        while (i + 1 < arr.size() && arr[i] < arr[i + 1]) i++;
        if (i == 0 || i == arr.size() - 1) return false;
        while (i + 1 < arr.size() && arr[i] > arr[i + 1]) i++;
        return i == arr.size() - 1;
    }
};
