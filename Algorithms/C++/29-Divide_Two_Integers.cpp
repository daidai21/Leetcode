// Runtime: 8 ms, faster than 18.75% of C++ online submissions for Divide Two Integers.
// Memory Usage: 8.2 MB, less than 72.00% of C++ online submissions for Divide Two Integers.
class Solution {
public:
    int divide(int dividend, int divisor) {
        if (dividend == INT_MIN && divisor == -1)
            return INT_MAX;
        int sign = (dividend > 0 ^ divisor > 0) ? -1 : 1;
        long dvd = labs(dividend);
        long dvs = labs(divisor);
        long quotient = 0;
        while (dvd >= dvs) {
            long tmp = dvs;
            long m = 1;
            while (tmp << 1 <= dvd) {
                tmp <<= 1;
                m <<= 1;
            }
            dvd -= tmp;
            quotient += m;
        }
        return sign * quotient;
    }
};
