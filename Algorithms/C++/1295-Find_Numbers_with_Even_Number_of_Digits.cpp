// Runtime: 8 ms, faster than 75.00% of C++ online submissions for Find Numbers with Even Number of Digits.
// Memory Usage: 8.9 MB, less than 100.00% of C++ online submissions for Find Numbers with Even Number of Digits.
class Solution {
public:
    int findNumbers(vector<int>& nums) {
        int even_cnt = 0;
        for (int num : nums) {
            int digit = 0;
            while (num > 0) {
                num /= 10;
                digit++;
            }
            even_cnt += digit % 2 == 0;
        }
        return even_cnt;
    }
};
