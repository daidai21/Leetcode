// Runtime: 0 ms, faster than 100.00% of C++ online submissions for Check if Binary String Has at Most One Segment of Ones.
// Memory Usage: 6.2 MB, less than 18.30% of C++ online submissions for Check if Binary String Has at Most One Segment of Ones.
class Solution {
public:
    bool checkOnesSegment(string s) {
        return s.find("01") == string::npos;
    }
};
