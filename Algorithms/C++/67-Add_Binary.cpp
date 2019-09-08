// Runtime: 8 ms, faster than 26.76% of C++ online submissions for Add Binary.
// Memory Usage: 9.3 MB, less than 54.54% of C++ online submissions for Add Binary.
class Solution {
public:
    string addBinary(string a, string b) {
        string res;
        int flag = 0;
        int i_a = a.length() - 1, i_b = b.length() - 1;
        while (i_a >= 0 || i_b >= 0 || flag) {
            int cur_val = 0;
            cur_val += i_a >= 0 && a[i_a] == '1';
            cur_val += i_b >= 0 && b[i_b] == '1';
            int old_flag = flag;
            flag = (cur_val + flag) / 2;
            int val = (cur_val + old_flag) % 2;
            res = to_string(val) + res;
            --i_a;
            --i_b;
        }
        return res;
    }
};
