// Runtime: 16 ms, faster than 15.35% of C++ online submissions for Fibonacci Number.
// Memory Usage: 8.2 MB, less than 100.00% of C++ online submissions for Fibonacci Number.
class Solution {
public:
    int fib(int N) {
        return N < 2 ? N : fib(N - 1) + fib(N - 2);
    }
};
