// Runtime: 52 ms, faster than 91.45% of C++ online submissions for Counting Bits.
// Memory Usage: 9.4 MB, less than 100.00% of C++ online submissions for Counting Bits.
class Solution {
public:
    vector<int> countBits(int num) {
        vector<int> res(num + 1, 0);
        for (int i = 1; i <= num; ++i) {
            int tmp = i, n = 0;
            while (tmp > 0) {
                if (tmp & 1 == 1)
                    ++n;
                tmp >>= 1;
            }
            res[i] = n;
        }
        return res;
    }
};


// Runtime: 52 ms, faster than 91.45% of C++ online submissions for Counting Bits.
// Memory Usage: 9.4 MB, less than 100.00% of C++ online submissions for Counting Bits.
class Solution {
public:
    vector<int> countBits(int num) {
        vector<int> res(num + 1, 0);
        for (int i = 1; i <= num; ++i)
            res[i] = res[i & (i - 1)] + 1;
        return res;
    }
};


// Runtime: 52 ms, faster than 91.45% of C++ online submissions for Counting Bits.
// Memory Usage: 9.6 MB, less than 81.70% of C++ online submissions for Counting Bits.
class Solution {
public:
    vector<int> countBits(int num) {
        vector<int> res(num + 1, 0);
        for (int i = 1; i <= num; ++i)
            res[i] = res[i >> 1] + (i & 1);  // Recursive formula
        return res;
    }
};
