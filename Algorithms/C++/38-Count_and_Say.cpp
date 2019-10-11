// Runtime: 4 ms, faster than 77.52% of C++ online submissions for Count and Say.
// Memory Usage: 8.7 MB, less than 93.06% of C++ online submissions for Count and Say.
class Solution {
public:
    string countAndSay(int n) {
        string result = "1";
        if (n == 1)
            return result;
        for (int j = 1; j < n; ++j) {
            string res;
            char tmp = result[0];
            int cnt = 1;
            for (int i = 1; i < result.size(); ++i) {
                if (tmp == result[i])
                    ++cnt;
                else {
                    res += to_string(cnt) + tmp;
                    tmp = result[i];
                    cnt = 1;
                }
            }
            res += to_string(cnt) + tmp;
            result = res;
        }
        return result;
    }
};
