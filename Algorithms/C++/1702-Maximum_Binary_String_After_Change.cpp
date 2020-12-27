// https://leetcode-cn.com/problems/maximum-binary-string-after-change/solution/c-jian-dan-gou-zao-by-francissoft-bxen/
class Solution {
public:
    string maximumBinaryString(string binary) {
        int ones = 0;
        bool flag = false;
        for (const char& ch : binary) {
            if (ch == '0')
                flag = true;
            if (flag && ch == '1')
                ones++;
        }
        if (!flag)
            return binary;
        string res(binary.size(), '1');
        res[binary.size() - ones - 1] = '0';
        return res;
    }
};
