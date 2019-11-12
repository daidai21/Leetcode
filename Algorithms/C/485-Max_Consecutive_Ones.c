// Runtime: 40 ms, faster than 63.16% of C online submissions for Max Consecutive Ones.
// Memory Usage: 8.6 MB, less than 100.00% of C online submissions for Max Consecutive Ones.
int findMaxConsecutiveOnes(int* nums, int numsSize){
    int ans = 0;
    int tmp = 0;
    for (int i = 0; i < numsSize; ++i)
        if (*(nums + i) == 1)
            tmp++;
        else {
            ans = ans > tmp ? ans : tmp;
            tmp = 0;
        }
    return ans > tmp ? ans : tmp;
}
