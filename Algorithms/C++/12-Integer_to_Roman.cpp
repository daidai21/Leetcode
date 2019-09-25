// Runtime: 12 ms, faster than 49.79% of C++ online submissions for Integer to Roman.
// Memory Usage: 11.1 MB, less than 36.84% of C++ online submissions for Integer to Roman.
class Solution {
public:
    string intToRoman(int num) {
        vector<int> values = {1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1};
        vector<string> numerals = {"M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"};
        string result;
        for (int i = 0; i < values.size(); ++i) {
            for (int j = 0; j < num / values[i]; ++j)
                result += numerals[i];
            num = num % values[i];
        }
        return result;
    }
};
