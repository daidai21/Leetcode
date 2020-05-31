// Runtime: 0 ms, faster than 100.00% of C++ online submissions for Number of Students Doing Homework at a Given Time.
// Memory Usage: 11 MB, less than 100.00% of C++ online submissions for Number of Students Doing Homework at a Given Time.
class Solution {
public:
    int busyStudent(vector<int>& startTime, vector<int>& endTime, int queryTime) {
        int res = 0;
        for (int i = 0; i < startTime.size(); ++i) {
            if (startTime[i] <= queryTime && endTime[i] >= queryTime)
                res++;
        }
        return res;
    }
};


// Runtime: 8 ms, faster than 58.68% of C++ online submissions for Number of Students Doing Homework at a Given Time.
// Memory Usage: 11 MB, less than 100.00% of C++ online submissions for Number of Students Doing Homework at a Given Time.
class Solution {
public:
    int busyStudent(vector<int>& startTime, vector<int>& endTime, int queryTime) {
        int res = 0;
        for (int i = 0; i < startTime.size(); ++i) {
            res += startTime[i] <= queryTime && endTime[i] >= queryTime;
        }
        return res;
    }
};
