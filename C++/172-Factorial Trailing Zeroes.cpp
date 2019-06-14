class Solution {
public:
    int trailingZeroes(int n) {
        int res = 0;
        for (long long i = 5; n / i > 0; i *= 5) {
            res += n / i;
        }
        return res;
    }
};


/*
    0来自10
    10可以来自 2 × 5
    我们需要说明5和2的所有，例如4×5=20…
    所以，如果我们把所有带5的数作为因子，我们将有足够多的偶数与它们配对，得到10的因子。
*/
