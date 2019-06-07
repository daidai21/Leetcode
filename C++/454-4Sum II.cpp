// Time Limit Exceeded
class Solution {
public:
    int fourSumCount(vector<int>& A, vector<int>& B, vector<int>& C, vector<int>& D) {
        int res = 0;
        for (int a : A) {
            for (int b : B) {
                for (int c : C) {
                    for (int d : D) {
                        if ((a + b + c + d) == 0)
                            res++;
                    }
                }
            }
        }
        return res;
    }
};


// unordered_map
// Runtime: 248 ms, faster than 53.10% of C++ online submissions for 4Sum II.
// Memory Usage: 47.8 MB, less than 30.12% of C++ online submissions for 4Sum II.
class Solution {
public:
    int fourSumCount(vector<int>& A, vector<int>& B, vector<int>& C, vector<int>& D) {
        int res = 0;
        unordered_map<int, int> AB;
        for (int a : A) {
            for (int b : B) {
                AB[a + b]++;
            }
        }
        for (int c : C) {
            for (int d : D) {
                res += AB[-c - d];
            }
        }
        return res;
    }
};
