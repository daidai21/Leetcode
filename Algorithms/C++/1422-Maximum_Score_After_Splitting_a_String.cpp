// Runtime: 0 ms, faster than 100.00% of C++ online submissions for Maximum Score After Splitting a String.
// Memory Usage: 6.3 MB, less than 86.75% of C++ online submissions for Maximum Score After Splitting a String.
// 两次for循环扫描
class Solution {
public:
    int maxScore(string s) {
        int right_one = 0;
        for (int i = 1; i < s.size(); ++i) {
            if (s[i] == '1') {
                right_one++;
            }
        }
        int left_zero = s[0] == '0' ? 1 : 0;
        int res = left_zero + right_one;
        for (int i = 1; i < s.size() - 1; ++i) {
            if (s[i] == '0') {
                left_zero++;
            } else if (s[i] == '1') {
                right_one--;
            }
            res = max(res, left_zero + right_one);
        }
        return res;
    }
};



/**
 * result = max(zeros_on_left + ones_on_right)
 * result = max(zeros_on_left + (total_ones - ones_on_left))
 * result = max(zeros_on_left - ones_on_left) + total_ones
 */
// Runtime: 0 ms, faster than 100.00% of C++ online submissions for Maximum Score After Splitting a String.
// Memory Usage: 6.4 MB, less than 86.75% of C++ online submissions for Maximum Score After Splitting a String.
class Solution {
public:
    int maxScore(string s) {
        int tmp = -s.size() - 1, // max(zeros_on_left - ones_on_left)
            ones = 0, // ones on left
            zeros = 0; // zeros on left
        for (int i = 0; i < s.size(); ++i) {
            if (s[i] == '0') zeros++; else ones++;
            if (i < s.size() - 1) tmp = max(zeros - ones, tmp);
        }
        return tmp + ones;
    }
};
