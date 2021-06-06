// 滑动窗口
// Type-1   中直接全部copy追加到后边，模拟
class Solution {
public:
    int minFlips(string s) {
        int n = s.size();
        s += s;
        std::string s0, s1;
        for (int i = 0; i < s.size(); ++i) {
            s0 += i % 2 ? '1' : '0';
            s1 += i % 2 ? '0' : '1';
        }
        int res = std::numeric_limits<int>::max(), res0 = 0, res1 = 0;
        for (int i = 0; i < s.size(); ++i) {
            if (s[i] != s0[i]) res0++;
            if (s[i] != s1[i]) res1++;
            if (i >= n) {
                if (s[i - n] != s0[i - n]) res0--;
                if (s[i - n] != s1[i - n]) res1--;
            }
            if (i >= n - 1) res = std::min({res, res0, res1});
        }
        return res;
    }
};
