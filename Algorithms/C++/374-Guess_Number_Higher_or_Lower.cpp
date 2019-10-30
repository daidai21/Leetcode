// Runtime: 0 ms, faster than 100.00% of C++ online submissions for Guess Number Higher or Lower.
// Memory Usage: 8.2 MB, less than 83.33% of C++ online submissions for Guess Number Higher or Lower.
// binary search
// Forward declaration of guess API.
// @param num, your guess
// @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
int guess(int num);

class Solution {
public:
    int guessNumber(int n) {
        long int l = 1, r = n;
        while (l <= r) {
            long int mid = (l + r) / 2;
            int tmp = guess(mid);
            if (tmp == 0)
                return mid;
            else if (tmp == -1)
                r = mid - 1;
            else
                l = mid + 1;
        }
        return 0; // not using all case
    }
};
