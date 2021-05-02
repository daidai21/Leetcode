// greedy
// 贪心
// Runtime: 0 ms, faster than 100.00% of C++ online submissions for Find the Minimum Number of Fibonacci Numbers Whose Sum Is K.
// Memory Usage: 6.4 MB, less than 32.73% of C++ online submissions for Find the Minimum Number of Fibonacci Numbers Whose Sum Is K.
class Solution {
public:
    Solution() {
        fibs.push_back(1);
        fibs.push_back(1);
        int tmp;
        while (true) {
            tmp = fibs[fibs.size() - 2] + fibs[fibs.size() - 1];
            if (tmp > 1e9) {
                break;
            }
            fibs.push_back(tmp);
        }
    }
    
    int findMinFibonacciNumbers(int k) {
        int cnt = 0;
        for (int i = fibs.size() - 1; i >= 0; --i) {
            if (fibs[i] <= k) {
                cnt++;
                k -= fibs[i];
            }
            if (k == 0) {
                break;
            }
        }
        return cnt;
    }

private:
    std::vector<int> fibs;
};
