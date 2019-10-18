// Runtime: 4 ms, faster than 75.92% of C++ online submissions for Sqrt(x).
// Memory Usage: 8.2 MB, less than 98.25% of C++ online submissions for Sqrt(x).
class Solution {
public:
    int mySqrt(int x) {
        return sqrt(x);
    }
};


// Runtime: 24 ms, faster than 9.75% of C++ online submissions for Sqrt(x).
// Memory Usage: 8.2 MB, less than 100.00% of C++ online submissions for Sqrt(x).
class Solution {
public:
    int mySqrt(int x) {
        long int i = 0;
        while (i * i <= x)
            ++i;
        return i - 1;
    }
};
