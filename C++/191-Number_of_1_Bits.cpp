class Solution {
public:
    int hammingWeight(uint32_t n) { // uint32_t是unsigned int
        int res = 0;
        while (n) {
            n = n & (n - 1);
            res++;
        }
        return res;
    }
};


class Solution {
public:
    int hammingWeight(uint32_t n) {
        return n == 0 ? 0 : 1 + hammingWeight(n & (n - 1));
    }
};
