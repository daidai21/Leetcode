// Runtime: 4 ms, faster than 52.83% of C++ online submissions for Number Complement.
// Memory Usage: 8.1 MB, less than 100.00% of C++ online submissions for Number Complement.
class Solution {
public:
    int findComplement(int num) {
        unsigned int mask = ~0;
        while (num & mask)
            mask <<= 1;
        return ~num & ~mask;
    }
};
