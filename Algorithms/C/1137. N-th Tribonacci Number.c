// Runtime: 20 ms, faster than 99.01% of Python3 online submissions for N-th Tribonacci Number.
// Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for N-th Tribonacci Number.
int tribonacci(int n){
    if (n == 0)
        return 0;
    else if (n < 2)
        return 1;
    else {
        int t0 = 0, t1 = 1, t2 = 1;
        for (int i = 0; i < n - 2; ++i) {
            int temp = t0;
            t0 = t1;
            t1 = t2;
            t2 = temp + t0 + t1;
        }
        return t2;
    }
}
