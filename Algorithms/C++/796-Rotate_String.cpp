// Runtime: 0 ms, faster than 100.00% of C++ online submissions for Rotate String.
// Memory Usage: 8.5 MB, less than 60.00% of C++ online submissions for Rotate String.
class Solution {
public:
    bool rotateString(string A, string B) {
        return A.size() == B.size() && (A + A).find(B) != string::npos;
    }
};


// Time: O(n)
// Runtime: 0 ms, faster than 100.00% of C++ online submissions for Rotate String.
// Memory Usage: 8 MB, less than 100.00% of C++ online submissions for Rotate String.
class Solution {
public:
    bool rotateString(string A, string B) {
        if (A.size() != B.size())
            return false;
        int i = 0, j = 0;
        while (i < A.size()) {
            if (A[i] == B[j]) {
                i++;
                j++;
            } else {
                if (j)
                    j = 0;
                else
                    i++;
            }
        }
        i = 0;
        while (j < A.size()) {
            if (A[i] != B[j])
                return false;
            i++;
            j++;
        }
        return true;
    }
};
