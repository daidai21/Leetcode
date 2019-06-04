// Runtime: 4 ms, faster than 92.23% of C++ online submissions for Reverse Integer.
// Memory Usage: 8.2 MB, less than 68.28% of C++ online submissions for Reverse Integer.
class Solution {
public:
    int reverse(int x) {
        int res = 0;
        while (x != 0) {
            if (res > INT_MAX / 10 || res < INT_MIN / 10) return 0;
            res = res * 10 + x % 10;
            x /= 10;
        }
        return res;
    }
};


// official
class Solution {
public:
    int reverse(int x) {
        int rev = 0;
        while (x != 0) {
            int pop = x % 10;
            x /= 10;
            if (rev > INT_MAX/10 || (rev == INT_MAX / 10 && pop > 7)) return 0;
            if (rev < INT_MIN/10 || (rev == INT_MIN / 10 && pop < -8)) return 0;
            rev = rev * 10 + pop;
        }
        return rev;
    }
};
