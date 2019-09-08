// Runtime: 0 ms, faster than 100.00% of C++ online submissions for Water and Jug Problem.
// Memory Usage: 8 MB, less than 100.00% of C++ online submissions for Water and Jug Problem.
class Solution {
public:
    bool canMeasureWater(int x, int y, int z) {
        return z == 0 || (x + y >= z && z % gcd(x, y) == 0);
    }

    int gcd(int x, int y) {
        return y == 0 ? x : gcd(y, x % y);
    }
};
