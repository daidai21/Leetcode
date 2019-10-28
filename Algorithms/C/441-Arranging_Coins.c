// Runtime: 16 ms, faster than 19.05% of C online submissions for Arranging Coins.
// Memory Usage: 6.9 MB, less than 100.00% of C online submissions for Arranging Coins.
int arrangeCoins(int n){
    int cnt = 0,
        i = 1;
    while (n - i >= 0) {
        cnt++;
        n -= i;
        i++;
    }
    return cnt;
}
