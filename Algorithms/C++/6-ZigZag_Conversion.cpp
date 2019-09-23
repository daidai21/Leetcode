// Runtime: 16 ms, faster than 46.54% of C++ online submissions for ZigZag Conversion.
// Memory Usage: 12.7 MB, less than 46.29% of C++ online submissions for ZigZag Conversion.
class Solution {
public:
    string convert(string s, int numRows) {
        if (numRows == 1)
            return s;
        vector<string> mat(numRows);
        int direct = 1;  // 1 is down, -1 is up
        int row = 0;
        for (char ch : s) {
            mat[row].push_back(ch);
            if (row == numRows - 1)
                direct = -1;
            else if (row == 0)
                direct = 1;
            row += direct;
        }
        for (int i = 1; i < numRows; ++i)
            mat[0] += mat[i];
        return mat[0];
    }
};
