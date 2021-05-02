// Runtime: 0 ms, faster than 100.00% of C++ online submissions for Student Attendance Record I.
// Memory Usage: 6 MB, less than 89.56% of C++ online submissions for Student Attendance Record I.
class Solution {
public:
    bool checkRecord(string s) {
        if (std::count(s.begin(), s.end(), 'A')  > 1) {
            return false;
        }
        if (s.find("LLL") != std::string::npos) {
            return false;
        }
        return true;
    }
};
