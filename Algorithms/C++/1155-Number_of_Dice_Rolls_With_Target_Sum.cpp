// 1155. Number of Dice Rolls With Target Sum




// Time Limit Exceeded
class Solution {
public:
    int numRollsToTarget(int d, int f, int target) {
        if (d == 0) {
            if (target == 0) {
                return 1;
            } else {
                return 0;
            }
        }
        int res = 0;
        for (int i = 1; i <= f; ++i) {
            res += numRollsToTarget(d - 1, f, target - i);
        }
        return res;
    }
};



// Runtime: 24 ms, faster than 60.16% of C++ online submissions for Number of Dice Rolls With Target Sum.
// Memory Usage: 17.8 MB, less than 5.09% of C++ online submissions for Number of Dice Rolls With Target Sum.
class Solution {
public:
    Solution() : mem(31, vector<int>(1001, 0)) {}
    
    int numRollsToTarget(int d, int f, int target, int res = 0) {
        if (d == 0 || target <= 0) return d == target;
        if (mem[d][target]) return mem[d][target] - 1;
        for (int i = 1; i <= f; ++i) {
            res = (res + numRollsToTarget(d - 1, f, target - i)) % 1000000007;
        }
        mem[d][target] = res + 1;
        return res;
    }

private:
    vector<vector<int>> mem;
};
