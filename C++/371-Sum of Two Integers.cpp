# 对数运算的性质
// Runtime: 0 ms, faster than 100.00% of C++ online submissions for Sum of Two Integers.
// Memory Usage: 8.4 MB, less than 5.15% of C++ online submissions for Sum of Two Integers.
class Solution {
public:
    int getSum(int a, int b) 
    {
        if(a < b) swap(a, b);
        if(a==INT_MAX && b==INT_MIN) return -1;
        return (log(pow(2, b) * pow(2, a)) / log(2));
    }
};
