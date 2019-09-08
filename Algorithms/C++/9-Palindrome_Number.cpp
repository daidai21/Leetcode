// Runtime: 12 ms, faster than 72.67% of C++ online submissions for Palindrome Number.
// Memory Usage: 8.1 MB, less than 94.55% of C++ online submissions for Palindrome Number.
class Solution {
public:
    bool isPalindrome(int x) {
        long int reversed_num = 0, temp = x;
        while (temp > 0) {
            reversed_num = reversed_num * 10 + temp % 10;
            temp /= 10;
        }
        return reversed_num == x;
    }
};
