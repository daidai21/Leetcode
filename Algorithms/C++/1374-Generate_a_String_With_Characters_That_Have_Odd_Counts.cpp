// 1374. Generate a String With Characters That Have Odd Counts


// Runtime: 0 ms, faster than 100.00% of C++ online submissions for Generate a String With Characters That Have Odd Counts.
// Memory Usage: 6.3 MB, less than 27.04% of C++ online submissions for Generate a String With Characters That Have Odd Counts.
class Solution {
public:
    string generateTheString(int n) {
        return n % 2 == 1 ? std::string(n, 'a') : (std::string(n - 1, 'a') + std::string(1, 'b'));
    }
};
