// Runtime: 0 ms, faster than 100.00% of C++ online submissions for String to Integer (atoi).
// Memory Usage: 8.4 MB, less than 71.64% of C++ online submissions for String to Integer (atoi).
class Solution {
public:
    int myAtoi(string str) {
        int ret = 0, 
            sign = 1, 
            i = str.find_first_not_of(' '), 
            base = INT_MAX / 10;
        if (i == -1) // empty string
            return 0;
        if (str[i] == '+' || str[i] == '-') {
            sign = str[i] == '+' ?: -1;
            ++i;
        }
        while (isdigit(str[i])) {
            if (ret > base || (ret == base && str[i] - '0' > 7)) 
                return sign > 0 ? INT_MAX : INT_MIN;
            ret = 10 * ret + (str[i++] - '0');
        }
        return sign * ret;
    }
};
