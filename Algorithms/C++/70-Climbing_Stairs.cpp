// Time Limit Exceeded
class Solution {
public:
    int climbStairs(int n) {
        if (n <= 2)
            return n;
        return climbStairs(n - 1) + climbStairs(n - 2);
    }
};


// Runtime: 0 ms, faster than 100.00% of C++ online submissions for Climbing Stairs.
// Memory Usage: 8.3 MB, less than 83.82% of C++ online submissions for Climbing Stairs.
class Solution {
public:
    int climbStairs(int n) {
        if (n <= 2)
            return n;
        vector<int> dp = {0, 1, 2};
        for (int i = 3; i <= n; ++i)
            dp.push_back(dp[i - 2] + dp[i - 1]);
        return dp[n];
    }
};


// Runtime: 0 ms, faster than 100.00% of C++ online submissions for Climbing Stairs.
// Memory Usage: 8.2 MB, less than 98.53% of C++ online submissions for Climbing Stairs.
class Solution {
public:
    int climbStairs(int n) {
        if (n <= 2)
            return n;
        int n1 = 1, n2 = 2;
        for (int i = 3; i <= n; ++i) {
            swap(n1, n2);
            n2 = n1 + n2;
        }
        return n2;
    }
};
