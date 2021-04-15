// 1394. Find Lucky Integer in an Array


// Runtime: 8 ms, faster than 53.03% of C++ online submissions for Find Lucky Integer in an Array.
// Memory Usage: 9.9 MB, less than 98.97% of C++ online submissions for Find Lucky Integer in an Array.
class Solution {
public:
    int findLucky(vector<int>& arr) {
        std::sort(arr.begin(), arr.end(), [](const int& a, const int& b) { return a > b; });
        int num = arr[0], cnt = 1;
        for (int i = 1; i < arr.size(); ++i) {
            if (num == arr[i]) {
                cnt++;
            } else if (num == cnt) {
                return cnt;
            } else {
                num = arr[i];
                cnt = 1;
            }
        }
        return cnt == num ? cnt : -1;
    }
};


// Runtime: 8 ms, faster than 53.03% of C++ online submissions for Find Lucky Integer in an Array.
// Memory Usage: 10.3 MB, less than 16.91% of C++ online submissions for Find Lucky Integer in an Array.
class Solution {
public:
    int findLucky(vector<int>& arr) {
        std::vector<int> mp(501, 0);
        for (const int& n : arr) mp[n]++;
        int res = -1;
        for (int i = 1; i < mp.size(); ++i) {
            if (i == mp[i]) res = std::max(res, i);
        }
        return res;
    }
};
