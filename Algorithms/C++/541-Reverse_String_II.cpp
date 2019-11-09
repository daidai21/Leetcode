// Runtime: 4 ms, faster than 97.48% of C++ online submissions for Reverse String II.
// Memory Usage: 9.6 MB, less than 60.00% of C++ online submissions for Reverse String II.
class Solution {
public:
    string reverseStr(string s, int k) {
        for (int start = 0; start < s.size(); start += 2 * k) {
            int left = start, right = min(left + k - 1, static_cast<int>(s.size()) - 1);
            while (left < right) {
                swap(s[left], s[right]);
                left++;
                right--;
            }
        }
        return s;
    }
};
