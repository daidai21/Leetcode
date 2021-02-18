// Time Limit Exceeded
class Solution {
    public int climbStairs(int n) {
        if (n == 1) {
            return 1;
        }
        if (n == 2) {
            return 2;
        }
        return climbStairs(n - 1) + climbStairs(n - 2);
    }
}

// Runtime: 0 ms, faster than 100.00% of Java online submissions for Climbing Stairs.
// Memory Usage: 35.6 MB, less than 83.67% of Java online submissions for Climbing Stairs.
class Solution {
    public int climbStairs(int n) {
        if (n <= 2) { // n == 1 || n == 2
            return n;
        }
        int[] tmp = new int[n + 1];
        tmp[1] = 1; tmp[2] = 2;
        for (int i = 3; i <= n; ++i) {
            tmp[i] = tmp[i - 1] + tmp[i - 2];
        }
        return tmp[n];
    }
}
